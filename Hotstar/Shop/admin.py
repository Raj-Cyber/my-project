from django.contrib import admin
from .models import Category,Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','availability','created','updated']
    list_editable = ['price','stock','availability']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10
admin.site.register(Product,ProductAdmin)