from django.contrib import admin
from .models import FoodProduct, ProductPrice, NutritionInformation
# Register your models here.

admin.site.register(FoodProduct)
admin.site.register(ProductPrice)
admin.site.register(NutritionInformation)