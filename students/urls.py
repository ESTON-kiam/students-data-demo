from django.urls import path
from students import views
urlpatterns = [
 path('', views.index, name="index"),
 path('insert', views.insertData, name="insertData"),
 path('update/<id>', views.updateData, name="updateData"),
 path('delete/<id>', views.deleteData, name="deleteData"),
]