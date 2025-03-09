from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['course', 'activity', 'term', 'starttime', 'endtime', 'days']
