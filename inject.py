from food.models import *
from openfoodfacts import *


Category.objects.all().delete()
Product.objects.all().delete()

categories = openfoodfacts.facets.get_categories()

for item in categories[:4]:
	cat_name = item['name']
	new_cat = Category(name=cat_name)
	new_cat.save()
	new_cat_id = getattr(new_cat, 'id')
	products = openfoodfacts.products.get_by_category(cat_name)
	for food_item in products:
		try:
			food_name = food_item['product_name']
			foot_nutri = food_item['nutriscore_score']
			new_product = Product(name=food_name, nutriscore=foot_nutri, category_id=new_cat_id)
			new_product.save()
			new_cat.products.add(new_product)
		except:
			pass

'''
products = openfoodfacts.products.get_all_by_category('Snack')
for item in products:
	print(item['product_name'])
#item = Product(name="test_code", nutriscore=4)
#item.save()
#print(Category.objects.all().values_list('id', 'name'))
lol = Category.objects.first()
print(lol.name)
print(lol.products.all().values_list('id', 'name'))
prout = Category.objects.last()
print(prout.name)
print(prout.products.all().values_list('id', 'name'))
'''