from django.contrib import admin
from store.models import Category,Product,Cart,CartItem,Order,OrderItem

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','created','updated']
    list_editable=['price','stock']
    list_per_page=5

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','name','email','total','token','created','updated']
    list_per_page=5

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order','product','quantity','price','created','updated']
    list_per_page=5

class CartAdmin(admin.ModelAdmin):
    list_display=['id']
    list_per_page=5

class CartItemAdmin(admin.ModelAdmin):
    list_display=['product','cart_id','quantity','active']
    list_per_page=5






#set ฐานข้อมูล สร้าง migrationขึ้นมา/
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)