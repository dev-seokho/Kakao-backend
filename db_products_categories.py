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

CSV_PATH = './products_categories.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        print(row)
        ProductCategory.objects.create(
            product = Product.objects.get(id=row['products_id']),
            main_category = MainCategory.objects.get(id=row['main_categories_id']),
            sub_category = SubCategory.objects.get(id=row['sub_categories_id'])
        )
