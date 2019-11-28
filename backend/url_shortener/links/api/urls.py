from django.urls import path
from .views import LinksListView, LinksCreateView

urlpatterns = [
    path('', LinksListView.as_view()),
    path('create/', LinksCreateView.as_view()),
]
