from django.urls import re_path
from backend import views

urlpatterns=[
    re_path(r'^projects$', views.projectAPI),
    re_path(r'^projects/([0-9]+)$', views.projectAPI),

    re_path(r'^users$', views.userAPI),
    re_path(r'^users/([0-9]+)$', views.userAPI),

    re_path(r'^contribution$', views.contributionAPI),
    re_path(r'^contribution/([0-9]+)$', views.contributionAPI),

    re_path(r'^register$', views.registerPage, name='register'),
    re_path(r'^login$', views.loginPage, name='login'),
    re_path(r'^home$', views.homePgae, name='home'),

    #re_path(r'^checkout$', views.checkout, name='checkout'),
]