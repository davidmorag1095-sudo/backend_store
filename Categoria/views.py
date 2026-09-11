from django.http import HttpResponse, JsonResponse
from .models import Category


def home(request):
    return HttpResponse()


def api_category(request):
    categorys= Category.objects.all()   
    data = []

    for category in categorys:
        data.append({
            'Name':category.name,
            'Description':category.description,
            'Active':category.active
        })
    return JsonResponse({'Categorys':data})

