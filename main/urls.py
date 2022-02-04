from django.urls import path, include
from .views import *


urlpatterns = [
    path("refill/", fill_database),
    path("index/", IndexView.as_view()),
    path("<language_code>/list/", PageListView.as_view()),
    path("list/<int:pk>/", PageDetailView.as_view()),
]