from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from .models import Products

# Create your views here.

def index(request):
    # username = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    # is_admin = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # mobile_no = models.CharField(max_length=15)
    # address = models.CharField(max_length=200)
    # country = models.CharField(max_length=15, default='United Kindom')
    # state = models.CharField(max_length=15)
    # postcode = models.CharField(max_length=10)
    if request.method == 'POST':
        post = request.POST
        username = post.get('username')
        first_name = post.get('first_name')
        last_name = post.get('last_name')
        email = post.get('email')
        password = post.get('password')
        mobile_no = post.get('mobile_no')
        address = post.get('address')
        country = post.get('country')
        state = post.get('state')
        postcode = post.get('postcode')
        # name = post.get('name')
        # name = post.get('name')
        # name = post.get('name')
        # name = post.get('name')

        description = post.get('description')
        price = post.get('price')

        # API endpoint URL
        url = 'http://127.0.0.1:8000/login/'

        # Payload to send to the API
        payload = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'mobile_no': mobile_no,
            'address': address,
            'country': country,
            'state': state,
            'postcode': postcode,
            # 'last_name': last_name,
            # 'last_name': last_name,
            # 'last_name': last_name,
            # 'last_name': last_name,
            # 'last_name': last_name,
            # 'last_name': last_name,
            # 'last_name': last_name,

        }

        # Make the POST request to the API
        response = requests.post(url, data=payload)

        # Handle the response from the API
        if response.status_code == 201:
            return redirect('index')  # Redirect on success
        else:
            return JsonResponse(response.json())  # Return error response

    return render(request, 'index.html')


# store/views.py


def product_detail(request, product_id):
    product = get_object_or_404(Products, pk=product_id)

    return render(request, 'product.html', {'product': product})
