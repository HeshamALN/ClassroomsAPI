from django.shortcuts import render
from rest_framework.generics import DestroyAPIView,RetrieveUpdateAPIView, ListAPIView,RetrieveAPIView, CreateAPIView
from classes.models import Classroom
from .serializers import DetailSerializer, ListSerializer,CreateSerializer,UpdateSerializer


# Create your views here.


class ListView(ListAPIView): #done tested
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer

class DetailView(RetrieveAPIView): #done tested
	queryset = Classroom.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class CreateView(CreateAPIView): #done pending testing
	serializer_class = CreateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)



class UpdateView(RetrieveUpdateAPIView): #done pending testing
	queryset = Classroom.objects.all()
	serializer_class = UpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class DeleteView(DestroyAPIView): #done tested
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'