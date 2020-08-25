from rest_framework import generics
from .models import ToDo
from .serializers import TodoSerializers

# Create your views here.


class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo(generics.RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializers

