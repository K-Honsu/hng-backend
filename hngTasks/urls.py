from . import views
from django.urls import path

urlpatterns = [
    path('api', views.HNGView.as_view(), name='slack-data-list'),
]

