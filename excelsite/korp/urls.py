from django.urls import path
from .views import *

urlpatterns = [

    # path('', redir ),
    # path('/korp/', redir),
    path('update/', update, name="update_ref", kwargs={"pagetitle":"Получение курсов по API"} ),
    path('<int:dayindex>/', kurs, name="kurs_ref", kwargs={"pagetitle":"Курсы валют USD, EUR"} ),
]

#handler404=pageNotFound
