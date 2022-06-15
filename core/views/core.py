# from rest_framework.views import APIView
# from core.services import RetailStores
# from utils.apiResponse import ApiResponse

# class RetailStoreView(APIView):
# 	def get(self, request):
# 		res = ApiResponse("Some error occured")

# 		product = str(request.GET.get("product", None))
# 		offset = int(request.GET.get("offset", 0))
# 		limit = int(request.GET.get("limit", 100))

# 		res = RetailStores.get(product=product, offset=offset, limit=limit)
# 		return Response(res.json())
