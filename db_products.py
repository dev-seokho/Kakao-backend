import csv
import os
import django
import sys

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_1st.settings")
django.setup()

from product.models import *

CSV_PATH = './products.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        print(row)

        hot_image_id = None if row['hot_image_id']=='NULL' else HotImage.objects.get(id=row['hot_image_id'])
        series_category_id = None if row['series_category_id']=='NULL' else SeriesCategory.objects.get(id=row['series_category_id'])

        Product.objects.create(
            name = row['name'],
            price = row['price'],
            detail = row['detail'],
            sub_detail = row['sub_detail'],
            stock = row['stock'],
            image_url = row['image_url'],
            created_at = row['created_at'],
            global_delivery = row['global_delivery'],
            sales_quantity = row['sales_quantity'],
            discount = row['discount'],
            discount_percentage = row['discount_percentage'],
            series_category = series_category_id,
            hot_image = hot_image_id
        )
