from rest_framework.views import APIView
from rest_framework.response import Response
from core.services import ProductInStores
from utils.apiResponse import ApiResponse


class PromotionView(APIView):
	def patch(self, request):
		res = ApiResponse("Some error occured")
		data = request.data

		retailStore = data["retailStore"]
		product = data["product"]
		promotion = data["promotion"]

		res = ProductInStores.putPromotion(retailStore=retailStore, product=product, promotion=promotion)
		return Response(res.json())


class ProductInStoreView(APIView):
	def get(self, request):
		res = ApiResponse("Some error occured")

		product = request.GET.get("product", None)

		if not product:
			res = ApiResponse("Product not passed")
		else:
			res = ProductInStores.get(product)

		return Response(res.json())

