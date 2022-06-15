from core.serializers import ProductSerializer
from core.models import Product
from utils.apiResponse import ApiResponse


class Products:
	def get(offset, limit):
		"""
		"""
		products = Product.objects.all()[offset:limit]
		data = ProductSerializer(products, many=True).data
		res = ApiResponse(success=True, message="Successfully retrieved products", data=data)
		return res
