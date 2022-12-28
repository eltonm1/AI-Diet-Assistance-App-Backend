from celery import shared_task
from .models import FoodProduct
#https://www.caktusgroup.com/blog/2021/08/11/using-celery-scheduling-tasks/
#https://www.codingforentrepreneurs.com/blog/celery-redis-django/


#celery -A food_products.celery worker -B --loglevel=info

@shared_task()
def add(x, y):
    foodProducts = FoodProduct.objects.all().order_by('name')
    for product in foodProducts:
        print(product.name, product.nutrition.energy)

    return x + y