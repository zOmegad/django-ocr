from django.core.management.base import BaseCommand
from food.models import Product, Category
from openfoodfacts import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        categories = openfoodfacts.facets.get_categories()
        print("Starting injection ...")
        progression = 0
        for item in categories[:25]:
            enum = 0
            cat_name = item['name']
            new_cat = Category(name=cat_name)
            new_cat.save()
            new_cat_id = getattr(new_cat, 'id')
            products = openfoodfacts.products.get_all_by_category(cat_name)
            for food_item in products:
                try:
                    food_name = food_item['product_name']
                    foot_nutri = food_item['nutriscore_score']
                    food_image = food_item['image_front_url']
                    food_url = food_item['url']
                    food_nutri_grade = food_item['nutriscore_grade']
                    new_product = Product(
                        name=food_name,
                        nutriscore=foot_nutri,
                        image=food_image,
                        nutriscore_grade=food_nutri_grade,
                        url=food_url,
                        category_id=new_cat_id)
                    new_product.save()
                    new_cat.products.add(new_product)
                    enum += 1
                    progression += 1
                    print("Injecting -> " + str(progression) + "/3750")
                    if enum == 150:
                        break
                except BaseException:
                    pass
                    print("Failed to inject this product")
