
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from products import views

urlpatterns = [
    path('accenture/', views.accenture, name='accenture'),

]

urlpatterns += staticfiles_urlpatterns()