from django.urls import path
from .views import student_list_create

urlpatterns = [
    path('', student_list_create, name='student-list-create'),
]