from rest_framework.generics import ListAPIView, CreateAPIView
from links.models import Links
from .serializers import LinksSerializer


class LinksListView(ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class LinksCreateView(CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
