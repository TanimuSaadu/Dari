from django import template
from products.models import Product 

register = template.Library()

@register.inclusion_tag('products/product.html')
def get_product_list():
	return {'my_products': Product.objects.all()}