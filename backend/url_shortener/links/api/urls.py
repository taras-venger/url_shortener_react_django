from django.urls import path
from .views import (LinksListView,
                    LinksCreateView,
                    redirect_view,
                    delete_expired)

urlpatterns = [
    path('', LinksListView.as_view()),
    path('create/', LinksCreateView.as_view()),
    path('delete_expired/', delete_expired),
    path('<slug:short_url>/', redirect_view)
]
