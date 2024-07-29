"""
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!
СТВОРЕННЯ ГІТ РЕПОЗИТОРІЯ!!!!!!!!!!!!!!

ВСЕ ЙДЕ З КОРОБКИ

ДЖАНГО - ЛЕГАСІ



pip install django

django-admin startproject mysite


python .\manage.py runserver
python .\manage.py runserver 8001

python .\manage.py startapp main


update mysite\main\views.py
```
from django.http import HttpResponse


def index(response):
    return HttpResponse('<h1>test message!</h1>')
```

create mysite/main/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```


update mysite/mysite/urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

Питання
що робить include в джанго?
чи є інші способи додати url? якщо так, в чому різниця?
path("start.", views.index, name="index") навіщо тут параметр nsme?
що зберігається у файлі settings.py ?
що означає models.CASCADE у рядку todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)?
яка різниця між migrate та makemigrations ?
extends приклади та список можилвостей {% extends 'main/base.html' %} ?
що таке csrf_token?
"""

"""
python .\manage.py createsuperuser
python .\manage.py makemigrations
python .\manage.py migrate

"""
