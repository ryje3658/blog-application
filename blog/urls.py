from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:pk>/', views.post, name='post'),
    path('category/<str:category>/', views.individual_category, name='individual_category'),
    path('results/', views.search, name='search'),
    path('archive/', views.archive, name='archive'),
    path('createpost/', views.createpost, name='createpost'),
    path('updatepost/<int:pk>', views.updatepost, name='updatepost'),
    path('deletepost/<int:pk>', views.deletepost, name='deletepost'),
]