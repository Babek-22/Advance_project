from django.contrib import admin
from .models import Contact,Category,Product,Settings,Logo,Type,Subscriber,Blog,About

# Register your models here.

admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Settings)
admin.site.register(Logo)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(About)
# admin.site.register(Subscribe)

# class ProductAdmin(admin.ModelAdmin):
#     list_display=('name','price','category','active')
#     list_filter=('category','active')
#     search_fields=('name','description')
#     list_editable=('price','active')
#     list_per_page=10
#     readonly_fields=('likes','views')

    # fieldsets=(
    #     ( '1',{
    #         'fields':('name','price','description','image')
    #     }),
    #     ( '2',{'classes':('collapse',),
    #         'fields':('likes','views','color',)
    #     })
    # )

# Change name admin panel

admin.site.site_header="My project"

# admin.site.register(Product,ProductAdmin)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     search_fields=('name', )

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     autocomplete=('category', )

# @admin.register(Subscriber)
# class SubsciberAdmin(admin.ModelAdmin):
#     list_display=('email','created_at')
#     search_fields=('email', )

admin.site.register(Subscriber)
    
# admin.site.register(News,NewsAdmin)




