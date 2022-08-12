from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index',views.index,name = 'index_page'),
    path('authorize', views.authorize, name = 'auth_page'),
    path('about', views.about, name = 'about_page')
]