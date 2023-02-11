from django.urls import path
from .views import *

app_name = 'register'

urlpatterns = [
    path("",EmployeeListView.as_view(),name='list-employee'),
    path("create/",CreateEmployeeFormView.as_view(),name='create-employee'),
    path("<int:pk>/",EmployeeDetailView.as_view(),name='detail-employee'),
    path("<int:pk>/update/",EmployeeUpdateView.as_view(),name='update-employee'),
    path("<int:pk>/delete/",EmployeeDeleteView.as_view(),name='delete-employee'),
    path("register/",RegistrationView.as_view(),name='register'),
]
