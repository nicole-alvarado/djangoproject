from django.urls import path
from . import views

# otra forma de importar:
# 1. from myapp.views import hello
# 2. path('', hello)

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
]