from django.test import TestCase

# Create your tests here.
# store/tests/test_api.py
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from .models import Category, Product, Order
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_category():
    client = APIClient()
    response = client.post('/api/category/', {'name': 'Electronics', 'description': 'Devices and gadgets.'})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Electronics'

@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(name='Electronics', description='Devices and gadgets.')
    client = APIClient()
    response = client.post('/api/product/', {
        'name': 'Laptop',
        'description': 'A personal computer.',
        'price': 999.99,
        'stock': 10,
        'category': category.id
    })
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_order_creation():
    category = Category.objects.create(name='Electronics', description='Devices and gadgets.')
    product = Product.objects.create(name='Laptop', description='A personal computer.', price=999.99, stock=2, category=category)
    user = User.objects.create_user(username="madhav1",email="madhav1@test.com")
    client = APIClient()
    response = client.post('/api/order/', {
        'user': user.id,
        'product': [product.id],
        'total_amount': product.price
    })
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_order_creation_with_insufficient_stock():
    category = Category.objects.create(name='Electronics', description='Devices and gadgets.')
    product = Product.objects.create(name='Laptop', description='A personal computer.', price=999.99, stock=0, category=category)
    user = User.objects.create_user(username="madhav1",email="madhav1@test.com")
    client = APIClient()
    response = client.post('/api/order/', {
        'user': user.id,
        'product': [product.id],
        'total_amount': product.price
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'out of stock' in str(response.data)

@pytest.mark.django_db
def test_order_creation_with_incorrect_price():
    category = Category.objects.create(name='Electronics', description='Devices and gadgets.')
    product = Product.objects.create(name='Laptop', description='A personal computer.', price=999.99, stock=2, category=category)
    user = User.objects.create_user(username="madhav1",email="madhav1@test.com")
    client = APIClient()
    response = client.post('/api/order/', {
        'user': user.id,
        'product': [product.id],
        'total_amount': 1000
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Please enter the correct total amount' in str(response.data)

@pytest.mark.django_db
def test_order_creation_with_invalid_user():
    category = Category.objects.create(name='Electronics', description='Devices and gadgets.')
    product = Product.objects.create(name='Laptop', description='A personal computer.', price=999.99, stock=2, category=category)
    user = User.objects.create_user(username="madhav1",email="madhav1@test.com")
    client = APIClient()
    invalid_user_id = user.id+1
    response = client.post('/api/order/', {
        'user': invalid_user_id,
        'product': [product.id],
        'total_amount': product.price
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert f'Invalid pk "{invalid_user_id}" - object does not exist.' in str(response.data)
