from django import template
from app.models import Order

from store.models import KingOrder

# register template tag
register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        try:
            qs = Order.objects.filter(user=user, ordered=False)  # orders by the user, excluding previous orders
            ss=KingOrder.objects.filter(user=user,ordered=False)
        
            if qs.exists() or ss.exists():
                return qs[0].items.count() + ss[0].items.count()
        except:
            return 0
    return 0
