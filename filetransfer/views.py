from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

class Login(APIView):
	def post(self,request):
		username=(request.data.get("username"))
		password=(request.data.get("password"))
		user=authenticate(username=username,password=password)
		if user is None:
			return Response({ "Status": "Error", "Message" : "Invalid Crediants" },status=200)
		else:
			if user.is_active:
				login(self.request, user)
				return Response({ "Status": "Success", "Message" : "Welcome" },status=200)


from rest_framework.generics import CreateAPIView

class CreateUser(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'Status': 'Success'}, status=201, headers=headers)


# class CreateUser(APIView):
# 	serializer_class = UserSerializer
# 	def post(self,request):
# 		print(request.data)
# 		ser=self.serializer_class(data=request.data)
# 		if ser.is_valid():
# 			ser.save()
# 			return Response({ "Status": "Success", "Message" : "SuccessFully Saved." },status=200)
# 		else:
# 			print(ser.errors)
# 			return Response({ "Status": "Error", "Message" : ser.errors },status=200)

		
		
		#{ Status = "Error", Message = "Invalid Data." };



class UploadFile(APIView):
	parser_class = (FileUploadParser,)
	def post(self,request):
		print(request.data)
		file_serializer = FileSerializer(data={"file":request.data.get("profile")})
		if file_serializer.is_valid():
			file_serializer.save()
			return Response({"status":"Success","message":"done"}, status=201)
		else:
			print(file_serializer.errors)
			return Response(file_serializer.errors, status=400)		
		#{'UserName': '', 'LoginName': '', 'Password': '', 'Email': '', 'ContactNo': '', 'Address': ''}
			print(request.data)


class SearchUser(APIView):
	def post(self,request):
		print(request.data)
		if request.data.get("name")=="abc":
			return Response({"status":"False","message":"nahi hai"},status=200)

		return Response({"status":"True","data":"id"},status=200)


