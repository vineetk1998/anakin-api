from rest_framework.views import APIView
from rest_framework.response import Response
from core.services import Products
from utils.apiResponse import ApiResponse


class ProductView(APIView):
	def get(self, request):
		res = ApiResponse("Some error occured")

		offset = int(request.GET.get("offset", 0))
		limit = int(request.GET.get("limit", 100))

		res = Products.get(offset=offset, limit=limit)
		return Response(res.json())

