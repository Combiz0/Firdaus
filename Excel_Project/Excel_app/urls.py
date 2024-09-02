from . import views
from django.urls import path

# from .views import CheckFileView
urlpatterns = [
    path('',views.add_email,name='add_email'),
    path('delete/<str:email>/', views.delete_email, name='delete_email'),
    path('check/<str:email>/', views.check_email, name='check_email'),
    # path('get-expiry/<str:email>/', views.check_email, name='manage-expiry'),/
]