import datetime
from django.core.checks.messages import Error
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm, ProfileForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from app.models import Order, OrderItem, Lesson, Item
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.utils.safestring import mark_safe
from .models import Account, FranchiseeOwners
from store.models import BillingAddress
from app.models import Order
from .models import PilotCertificates as certificate
from .forms import certificate_form
from io import BytesIO
from django.views import View
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from store.forms import CheckoutForm
from jobsportal.models import UserMembership, membership

@csrf_protect
@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect("app:home")


# Login and Signup View
@csrf_protect
@csrf_protect
def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("app:home")

    # Login
    if request.method == 'POST' and 'login' in request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            # print("valid")
            if user is not None:

                if user.is_active:
                    login(request, user)
                    if request.session.get('productslug', False):
                        s = request.session.get('productslug')
                        del request.session['productslug']
                        return redirect("store:add-to-cart", slug=s)
                    return redirect("app:home")
                else:
                    messages.warning(
                        request, 'Please verify your email address to login!')
                    return redirect('login')

        else:
            try:
                acc = Account.objects.get(email=request.POST['email'])
                if acc.is_active:
                    context['message'] = 'Please enter correct email and password !'
                else:
                    context['message'] = 'Email address not verified!'
                    messages.warning(
                        request, 'Please verify your email address to login.')
            except Account.DoesNotExist:
                context['message'] = 'Please enter correct email and password !'
            context['login_form'] = form
            context['signup_form'] = SignUpForm()

    # Signup
    elif request.method == 'POST' and 'signup' in request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Account Confirmation mail
            current_site = get_current_site(request)  # current site domain
            mail_subject = 'Activate your IID Account'
            html_message = render_to_string('account/account_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })

            plain_message = strip_tags(html_message)

            print("Plain message: ", plain_message)
            # This will have no effect is you have set DEFAULT_FROM_EMAIL in settings.py
            from_email = None
            to_email = form.cleaned_data.get('email')
            fail_silently = False  # Set to true when Debug is False

            send_mail(mail_subject, plain_message, from_email, [
                      to_email], fail_silently, html_message=html_message)

            messages.info(request, mark_safe("A verification link has been sent to your email account" "<br />"
                                             "Please confirm your email address to complete the registration"))

            return redirect("login")

        else:
            context['login_form'] = LoginForm()
            context['signup_form'] = form

    # get request, display both signup and login forms
    else:
        form = LoginForm()
        from1 = SignUpForm()
        context['login_form'] = form
        context['signup_form'] = from1
    return render(request, 'account/login.html', context)


# Account Activate/Email Confirm View
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        # Welcome Email
        subject = "Welcome to IID"
        html_message = render_to_string('app/welcome_email.html',
                                        {'name': user.first_name + " " + user.last_name,
                                         'courses_url': request.build_absolute_uri(reverse('app:courses')),
                                         'contact_url': request.build_absolute_uri(reverse('app:contact'))})
        plain_message = strip_tags(html_message)
        # This will have no effect is you have set DEFAULT_FROM_EMAIL in settings.py
        from_email = None
        to = user.email  # This is a string, will be sent as a list
        fail_silently = False  # True in production

        send_mail(subject, plain_message, from_email, [
                  to], fail_silently, html_message=html_message)

        # Welcome Notification
        messages.success(request, 'Your account has been verified.')
        return redirect('app:home')
    else:
        messages.warning(
            request, 'Sorry, verification failed! Contact us if the issue persists.')
        return redirect('app:home')


@login_required(login_url='/login/')
@csrf_protect
@csrf_exempt
def profile_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("app:home")

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("account:profile")
        else:
            context['profile_form'] = form
    else:
        form = ProfileForm(
            initial={
                "email": request.user.email,
                "phone": request.user.phone,
                "country": request.user.country,
                "dob": request.user.dob,
                "hq": request.user.hq,

            }
        )

    try:
        ss = BillingAddress.objects.get(user=request.user)

        context['temp'] = ss

    except:

        context['t'] = True

    context['profile_form'] = form

    return render(request, 'account/profile.html', context)


@login_required(login_url='/login/')
def MyCourses(request):
    try:
        order_item = OrderItem.objects.filter(user=request.user, ordered=True)
        # courses = OrderItem
        context = {'order_items': order_item}
        if not order_item:
            messages.info(request, "You haven't purchased any course yet!")
            context['flag'] = True  # True if no courses present
        return render(request, "account/mycourses.html", context)

    except ObjectDoesNotExist:
        context = {'flag': True}
        messages.info(request, "You haven't purchased any course yet!")
        return render(request, "account/mycourses.html", context)


@login_required(login_url='/login/')
def LessonList(request, slug):
    try:
        bought_courses = Item.objects.filter(
            orderitem__user=request.user, orderitem__ordered=True)  # Purchased courses
        course = Item.objects.get(slug=slug)  # course user requesting to view
        context = {}
        if course in bought_courses:
            order_item = OrderItem.objects.get(user=request.user, item=course)
            if order_item.course_age():
                lessons = Lesson.objects.filter(course=course)
                context = {'course': course, 'lessons': lessons}
            else:
                messages.info(request, "Course Expired!")
        else:
            messages.info(request, "You haven't purchased this course!")
        return render(request, "account/lesson_list.html", context)
    except ObjectDoesNotExist:
        return redirect("app:error")


def changeaddress(request):

    form = CheckoutForm()

    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']

            try:
                ss = BillingAddress.objects.get(user=request.user)

                if ss:
                    ss.address_1 = address_1
                    ss.address_2 = address_2
                    ss.city = city
                    ss.state = state
                    ss.zip_code = zip_code
                    ss.save()

                else:
                    ss.address_1 = address_1
                    ss.address_2 = address_2
                    ss.city = city
                    ss.state = state
                    ss.zip_code = zip_code
                    ss.save()

                ss.save()
            except:
                billing_address = BillingAddress(
                    user=request.user,
                    name=request.user,
                    address_1=address_1,
                    address_2=address_2,
                    city=city,
                    state=state,
                    zip_code=zip_code


                )

                billing_address.save()

            return redirect('account:profile')

        return redirect('account:profile')

    return render(request, "account/changeaddress.html", {"form": form})


@login_required(login_url='/login/')
def Proceed(request):

    form = CheckoutForm()

    if request.method == "POST":

        form = CheckoutForm(request.POST or None)

        if form.is_valid():
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']

            billing_address = BillingAddress(
                user=request.user,
                name=request.user,
                address_1=address_1,
                address_2=address_2,
                city=city,
                state=state,
                zip_code=zip_code
            )

            billing_address.save()

        return redirect("app:checkout")

    return render(request, "account/add_address.html", {"form": form})


def franchiseportal(request):

    try:
        s1 = FranchiseeOwners.objects.get(user=request.user)
        s3 = len(s1.certificate_students.filter(completed=True))

        s2 = True

        return render(request, "account/franchise.html", {'s1': s1, 's2': s2, 's3': s3})
    except:
        s2 = False
        return render(request, "account/franchise.html", {'s2': s2})


def certificategen(request):

    form = certificate_form()

    if request.method == "POST":
        s1 = FranchiseeOwners.objects.get(user=request.user)

        form = certificate_form(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            Address = form.cleaned_data['Address']
            Dob = form.cleaned_data['dob']
            Photo_ID = form.cleaned_data['Photo_ID']
            sex = form.cleaned_data['sex']
            photo = form.cleaned_data['img']
            category = form.cleaned_data['category']
            blank = form.cleaned_data['blank']

            ss = certificate(
                name=name,
                Address=Address,
                certificate_number="777",
                Photo_ID_detail=Photo_ID,
                sex=sex,
                category=category,
                photo=photo,
                Dob=Dob,
                Photo_ID=blank
            )

            ss.save()
            s1.certificate_students.add(ss)
            s1.save()

            return render(request, "account/genrate.html")

        else:
            pass

    context = {"form": form}
    return render(request, "account/studentform.html", context)


def check1(request):

    s = FranchiseeOwners.objects.get(user=request.user)
    s1 = s.certificate_students.filter(completed=True)

    return render(request, "account/certificate_form1.html", {'s': s1})


def show(request):
    sam = certificate.objects.filter(completed=False).last()

    params = {

        'sales': sam,
        'request': request
    }

    return Render.render('account/pdf.html', params)



def certificate_numberss(request, slug):

    try:
        sam = certificate.objects.get(slug=slug)

        params = {
            'sales': sam,
        }

        return Render.render('account/pdf.html', params)

    except:
        return HttpResponse("404 bad error")


@login_required(login_url='/login/')
def Proceed1(request, slug):
    if True:

        franchasice = FranchiseeOwners.objects.get(user=request.user)
        s1 = franchasice.certificate_students.get(slug=slug, completed=True)

        params = {
            'sales': s1
        }

        return Render.render('app/pdf.html', params)

    else:
        return HttpResponse("Error")

@login_required
def subscription(request):
    
    check=UserMembership.objects.filter(usermembership__email=request.user).first()
    
    if not check:
        s2=membership.objects.get(membership_type='Free')
        s1=Account.objects.get(email=request.user)
        check=UserMembership.objects.create(usermembership=s1,membership_method=s2,active=False)
        check.save()

    membership1=membership.objects.all()
    
    context={
        'membership1':membership1, 
        'check':check
    }
    
    try:
        if  str(check.membership_method) == str('Free'):
            messages.info(request, "You are using free account")
            return render(request,"account/subscriptionpage.html",context)
        
        else:
            return render(request,"account/subscriptionpage.html",context)
            
    except:
        messages.info(request, "You are using free account")
        return render(request,"account/subscriptionpage.html",context)



def subscriptioncheck(request,slug):
    check=UserMembership.objects.filter(usermembership__email=request.user).first()

    if str(check.membership_method) == str(slug):
        messages.info(request, "You are currently using this account")
        return redirect('account:subscription')

    return redirect("app:CheckoutView_subscription",pk=slug) 

def show_for_Recuiter(request):
    print(subscription)

