from django.urls import path
from .views import *

urlpatterns = [
	path('',home, name='home'),
	path('about/',about, name='about'),
	path('checkout/',checkout, name='checkout'),
	path('faqs/',faqs, name='faqs'),
	path('help/',helps, name='help'),
	path('payment/',payment, name='payment'),
	path('privacy/',privacy, name='privacy'),
	path('product/',product, name='product'),
	path('contact/',contact, name='contact'),
]