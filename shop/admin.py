from django.contrib import admin


from .models import Category, Product, Characteristics

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Characteristics)
