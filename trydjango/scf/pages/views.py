from django.shortcuts import render

from django.http import HttpResponse


def home_view(request, *args, **kwargs):
	# print(request.user)
	# print(args, kwargs)
	context = {
		'mystr': 'This is the context',
		'list': [2,3,4,5,'hello world']
	}
	return render(request, 'products/home.html', context)


def about_view(request, *args, **kwargs):
	return render(request, 'products/about.html', {})


def contact_view(request, *args, **kwargs):
	return render(request, 'products/contact.html', {})
