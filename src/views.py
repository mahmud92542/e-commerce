from django.shortcuts import render

# Create your views here.

def home(request):
	return render (request,'src/index.html')

def about(request):
	return render (request,'src/about.html')

def checkout(request):
	return render (request,'src/checkout.html')

def contact(request):
	return render (request,'src/contact.html')

def faqs(request):
	return render (request,'src/faqs.html')

def helps(request):
	return render (request,'src/help.html')

def payment(request):
	return render (request,'src/payment.html')

def privacy(request):
	return render (request,'src/privacy.html')

def product(request):
	return render (request,'src/product.html')

def product2(request):
	return render (request,'src/product2.html')

def single(request):
	return render (request,'src/single.html')

def single2(request):
	return render (request,'src/single2.html')

def terms(request):
	return render (request,'src/terms.html')