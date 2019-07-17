from django.urls import path
from .views import *

urlpatterns = [
	path('',home, name='home'),
	path('about/',about, name='about'),
	path('checkout/',checkout, name='checkout'),
	path('contact/',contact, name='contact'),
	path('faqs/',faqs, name='faqs'),
	path('help/',helps, name='help'),
	path('payment/',payment, name='payment'),
	path('privacy/',privacy, name='privacy'),
	path('product/',product, name='product'),
	path('product2/',product2, name='product2'),
	path('single/',single, name='single'),
	path('single2/',single2, name='single2'),
	path('terms/',terms, name='terms'),
	
]