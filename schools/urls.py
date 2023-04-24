from django.urls import re_path
from schools import views

urlpatterns=[re_path(r'^schools$',views.SchoolsApi),re_path(r'^schools/([0-9]+)$',views.SchoolsApi)]