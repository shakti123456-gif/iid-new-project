from django.shortcuts import render
from django.db import IntegrityError

# Create your views here.
from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView,View
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model=Item
    template_name = "catalogue.html"
    paginated_by=1


class ItemDetailView(DetailView):
    #login_url = '/login/'
    model=Item
    template_name="product.html"
    

def add_to_cart(request,slug):

    current_user=request.user
    if str(current_user) == 'AnonymousUser':
        request.session['productslug'] = str(slug)

        return redirect("login")
    
    item=get_object_or_404(Item,slug=slug)

    order_item,created=KingOrderItems.objects.get_or_create(item=item,user=request.user,ordered=False)

    order_qs=KingOrder.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity+=1
            messages.info(request,"Item quantity updated")
            order_item.save()
        else :
            messages.info(request,"This item was added to your cart.")
            order.items.add(order_item)
    else:
        ordered_date=timezone.now()
        order=KingOrder.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"Item quantity updated  ")

    return redirect("app:order-summary")


class OrderSummaryView(View):
    def get(self,*args,**kwargs):

            order=KingOrder.objects.get(user=self.request.user,ordered=False)
            context={
                'objects':order
            }
            return render(self.request,'order_summary.html',context) 
    

@login_required
def remove_item_from_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)

    order_qs=KingOrder.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            
            order_item=KingOrderItems.objects.filter(
                item=item,user=request.user,ordered=False)[0]


            if order_item.quantity>1:
                order_item.quantity-=1
                order_item.save()
                messages.info(request,"Item quantity updated")
            else:
                order.items.remove(order_item)

            return redirect('app:order-summary')
        else:
 
            return redirect("app:order-summary")
           
    else:
        messages.info(request,"You do not have an active order")
        
    return redirect("app:order-summary")


@login_required
def remove_from_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)

    order_qs=KingOrder.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            
            order_item=KingOrderItems.objects.filter(
                item=item,user=request.user,ordered=False)[0]

            order_item.quantity=1
            order_item.save()           
            order.items.remove(order_item)
            messages.info(request,"This Item was removed from your cart")
            return redirect("app:order-summary")
        else:
            messages.info(request,"This item was removed from your cart ")
            return redirect("store:products",slug=slug)
           
    else:
        messages.info(request,"You do not have an active order")
        return redirect("store:products",slug=slug)
    return redirect("store:products",slug=slug)




def active_order(request):

    try :
        order_qs=KingOrder.objects.filter(user=request.user,ordered=True).order_by('-ordered_date')
        
        if order_qs:
            return render(request,"orderhistory.html",{"order_qs":order_qs ,"show":True})
        
        else:
            messages.info(request,"Your order history is empty!")
            return render(request,"orderhistory.html",{"show":False})
    
    except:
        messages.info(request,"Your order history is empty!")
        return render(request,"orderhistory.html",{"show":False})    

