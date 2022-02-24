from django.urls import path    
from . import views

urlpatterns =[
    path('', views.userlist, name="users"),
    path('create',views.createuser,name="create"),
    path('delete/<str:pk>/',views.deleteUser,name="delete"),
    path('update/<str:pk>/',views.updateUser,name="update"),

]