from django.urls import path
from .views import LinksListView, LinksCreateView, redirect_view

urlpatterns = [
    path('', LinksListView.as_view()),
    path('create/', LinksCreateView.as_view()),
    path('<slug:short_url>/', redirect_view)
]
