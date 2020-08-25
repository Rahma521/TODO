from rest_framework import serializers
from.models import ToDo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        field = ('id', 'title', 'body')