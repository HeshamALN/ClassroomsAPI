from rest_framework import serializers
from classes.models import Classroom


class ListSerializer(serializers.ModelSerializer): #done
	class Meta:
		model = Classroom
		fields = ['subject','year','teacher','id']



class DetailSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Classroom
		fields = ['subject','year','teacher','id','name']		


class CreateSerializer(serializers.ModelSerializer): #fix
    class Meta:
        model = Classroom
       	fields = ['subject','year','name']



class UpdateSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Classroom
		fields = ['subject','year','name']	
