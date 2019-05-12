from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from .serializers import FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class Login(APIView):
	def post(self,request):
		print(request.data)
		return Response({ "Status": "Success", "Message" : "gautam" },status=200)

class CreateUser(APIView):
	def post(self,request):
		#{'UserName': '', 'LoginName': '', 'Password': '', 'Email': '', 'ContactNo': '', 'Address': ''}
		print(request.data)
		return Response({ "Status": "Success", "Message" : "SuccessFully Saved." },status=200)
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


