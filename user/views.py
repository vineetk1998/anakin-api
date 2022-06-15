import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class UserView(APIView):

	def post(self, request):
		"""For creating user"""
		res = {"message": "Some error occured", "success": False}
		if request.method == "POST":
			data = request.data
			print(data)
			username = data["username"]
			password = data["password"]
			try:
				user = User.objects.create_user(username=username, password=password)
				if user is not None:
					login(request, user)
					res = {"message": "Successfully registered user and logged in", "success": True}
			except Exception as ex:
				# do some logging
				print(str(ex))
		return Response(res)


class LoginView(APIView):

	def post(self, request):
		"""For login"""
		res = {"message": "Some error occured", "success": False}
		if request.method == "POST":
			data = request.data
			username = data["username"]
			password = data["password"]

			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				res = {"message": "Logged in successfully", "success": True}
			else:
				# Return an 'invalid login' error message.
				res = {"message": "Invalid login credentials", "success": False}
		# the login is a  GET request, so just show the user the login form.
		return Response(res)

