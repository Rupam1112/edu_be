from django.urls import re_path
from users import views

urlpatterns=[re_path(r'^users$',views.UsersApi),
             re_path(r'^users/([0-9]+)$',views.UsersApi),
             re_path(r'^login$',views.Login),
             re_path(r'^usersBySchool/([0-9]+)$', views.UsersBySchool)]