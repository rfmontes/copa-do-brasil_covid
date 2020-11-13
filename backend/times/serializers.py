from rest_framework import serializers
from django.contrib.auth.models import User
from times.models import Time


class TimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Time
        fields = ['id', 'nome_time', 'votos', 'created_at', 'ativo']
        # fields = '__all__'
