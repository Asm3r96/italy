from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return render (request, "italy/index.html")
from .models import *

import italy
from . import views
from .models import *

def index(request):
    # list of products availables
    meals = Meal.objects.all()
    categories = Category.objects.all()
    # checking if there are any products
    empty = False
    if len(meals) == 0:
        empty = True
    return render(request, "italy/index.html", {
        "meals": meals,
        "categories": categories,
        "empty": empty
    })


def meals(request):
    # list of products availables
    meals = Meal.objects.all()
    categories = Category.objects.all()
    # checking if there are any products
    empty = False
    if len(meals) == 0:
        empty = True
    return render(request, "italy/meals.html", {
        "meals": meals,
        "categories": categories,
        "empty": empty
    })
    