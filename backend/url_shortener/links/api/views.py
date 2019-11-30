from rest_framework.generics import ListAPIView, CreateAPIView
from links.models import Links
from .serializers import LinksSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


class LinksListView(ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class LinksCreateView(CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


def redirect_view(request, short_url=None, *args, **kwargs):
    obj = get_object_or_404(Links, short_url=short_url)
    return HttpResponseRedirect(obj.original_url)
