from django.urls import path
from . import views

# first_app/
urlpatterns = [
    path('', views.example_view),
    path('variable/', views.variable_view),
]
