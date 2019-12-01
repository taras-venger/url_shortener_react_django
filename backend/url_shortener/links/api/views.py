from rest_framework.generics import ListAPIView, CreateAPIView
from links.models import Links
from .serializers import LinksSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date


class LinksListView(ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class LinksCreateView(CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


def redirect_view(request, short_url=None, *args, **kwargs):
    obj = get_object_or_404(Links, short_url=short_url)
    return HttpResponseRedirect(obj.original_url)


def delete_expired(request):
    queryset = Links.objects.all()
    today = date.today()
    for q in queryset:
        if (date.today() - q.created_on).days > q.lifetime_days:
            q.delete()
    return HttpResponse('remove expired links')
