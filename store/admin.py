from django.contrib import admin

from .models import * 


class ProductAdmin(admin.ModelAdmin):

    list_display = ('user', 'ordered','ordered_date','shipment')
    search_fields = ("user", )
    list_filter = ("shipment", )


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ("title", )


admin.site.register(Item,ItemAdmin)
admin.site.register(KingOrder,ProductAdmin)
admin.site.register(KingOrderItems)
admin.site.register(BillingAddress)
