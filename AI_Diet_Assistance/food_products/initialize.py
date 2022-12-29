from .models import FoodProduct
import pandas as pd



# print(price_watch_data.head())
def initialize():

    code_mapping = {}
    with open('food_products/all_code.txt') as all_code:
        codes = all_code.readlines()
        for code in codes:
            price_watch_code, barcode = code.split(',')
            barcode = barcode.split()[0] if len(barcode.split()) > 0 else ""
            if barcode == "":
                continue
            # print(price_watch_code, barcode)
            code_mapping[price_watch_code] = barcode


    price_watch_data = pd.read_csv("food_products/price.csv")
    price_watch_data = price_watch_data.groupby(['Product Code', 'Category 1', 
                'Category 2', 'Category 3', 'Brand', 'Product Name' ]

            ).agg(lambda x: list(x))#.apply(list)#.reset_index()

    # x = price_watch_data.head(1)
    price_watch_data =price_watch_data.reset_index()
    for index, row in price_watch_data.iterrows():
        product_name = row['Product Name']
        price_watch_code = row['Product Code']
        barcode = code_mapping.get(price_watch_code)
        category_1 = row['Category 1']
        category_2 = row['Category 2']
        category_3 = row['Category 3']
        brand = row['Brand']
        
        product = FoodProduct(name=product_name, 
                barcode=barcode, pricewatchcode=price_watch_code, 
                brand=brand, category_1 = category_1, 
                category_2 = category_2, category_3 = category_3)
        product.save()
        # print(product_name, price_watch_code, barcode, brand)

if __name__ == "__main__":
    initialize()
