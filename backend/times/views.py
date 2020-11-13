from times.models import Time
from times.serializers import TimeSerializer
from rest_framework import viewsets


class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
