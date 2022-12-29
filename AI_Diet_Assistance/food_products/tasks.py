from celery import shared_task
from .models import FoodProduct
import pandas as pd
#https://www.caktusgroup.com/blog/2021/08/11/using-celery-scheduling-tasks/
#https://www.codingforentrepreneurs.com/blog/celery-redis-django/


#celery -A food_products.celery worker -B --loglevel=info

@shared_task()
def add(x, y):
    foodProducts = FoodProduct.objects.all().order_by('name')
    for product in foodProducts:
        print(product.name, product.nutrition.energy)

    return x + y

@shared_task()
def update_price():
    price_watch_data = pd.read_csv("https://online-price-watch.consumer.org.hk/opw/opendata/pricewatch_en.csv")
    price_watch_data = price_watch_data.groupby(['Product Code', 'Category 1', 
                'Category 2', 'Category 3', 'Brand', 'Product Name' ]

            ).agg(lambda x: list(x))
    price_watch_data = price_watch_data.reset_index()  
    for index, row in price_watch_data.iterrows():
        price_watch_code = row['Product Code']

        #Find product from db
        try:
            product = FoodProduct.objects.get(pricewatchcode=price_watch_code)

            for price, supermarket in zip(row['Price'], row['Supermarket Code']):
                # print(price, supermarket)
                if not price.replace('.','',1).isdigit():
                    continue
                # product_price = ProductPrice(
                #             price=price, 
                #             supermarket=supermarket.capitalize()).save()

                product.product_price.create(price=price, 
                            supermarket=supermarket.capitalize())

        except FoodProduct.DoesNotExist:
            continue