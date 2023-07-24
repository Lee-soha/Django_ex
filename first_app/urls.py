from django.urls import path
from . import views

# first_app/
urlpatterns = [
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>', views.add_view),
]
