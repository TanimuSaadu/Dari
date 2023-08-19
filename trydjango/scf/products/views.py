from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product


def product_create_view(request):
    print(request.user)
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def product_update_view(request, id):
	obj = get_object_or_404(Product, id=id)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, 'products/product_create.html', context)



def product_detail_view(request, id):
	obj = get_object_or_404(Product, id=id)
	context = {
		'objects': obj
	}
	return render(request, 'products/product_detail.html', context)


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'list_obj': queryset
	}
	return render(request, 'products/product_list.html', context)


def product_delete_view(request,id):
	obj = Product.objects.get(id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('../../')
	context = {
		'objects': obj
	}
	return render(request, 'products/product_delete.html', context)


# def product_dynamic_view(request,id):
# 	# obj = Product.objects.get(id=id)
# 	# obj = get_object_or_404(Product, id=id)
# 	try:
# 		obj = Product.objects.get(id=id)
# 	except Product.DoesNotExist:
# 		raise Http404
# 	context = {
# 		'objects': obj
# 	}
# 	return render(request, 'products/product_detail.html', context)


# def render_initial_data(request):
# 	initial_data = {
# 		'title': 'this is awesome title'
# 	}
# 	obj = Product.objects.get(id=1)
# 	form = ProductForm(request.POST or None, instance=obj)
# 	if form.is_valid():
# 		form.save()
# 	context = {
# 		'form': form
# 	}
# 	return render(request, 'products/product_create.html', context)


# def product_create_view(request):
# 	my_form = RawProductForm()
# 	if request.method == 'POST':
# 		my_form = RawProductField(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context = {
# 		'form': my_form
# 	}
# 	return render(request, 'products/product_create.html', context)


# def product_create_view(request):
# 	if request.method == 'POST':
# 		# print(request.GET)
# 		# print(request.POST)
# 		my_title = request.POST.get('title')
# 		print(my_title)
# 	context = {}
# 	return render(request, 'products/product_create.html', context)
