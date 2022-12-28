from django.contrib import admin
from .models import FoodProducts, ProductPrice, NutritionInformation
# Register your models here.

admin.site.register(FoodProducts)
admin.site.register(ProductPrice)
admin.site.register(NutritionInformation)