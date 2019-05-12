from rest_framework import serializers
from django.contrib.auth.models import User
from .models import File

class FileSerializer(serializers.ModelSerializer):
	# sentby=serializers.CharField()
	# sentto=serializers.CharField()

	# def validate_sentto(self,data):
		
	
	# def get_sentby(self, obj):
	# 	request = getattr(self.context, 'request', None)
	# 	if request:
	# 		return request.user
	class Meta:
		model = File
		fields = ("file",)

	# def create(self, validated_data):
	# 	obj = File.objects.create(**validated_data)
 #    	obj.save(foo=validated_data['foo'])
 #    	return obj	


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


