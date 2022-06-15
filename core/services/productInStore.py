from core.serializers import ProductInStoreSerializer
from core.models import ProductInStore
from utils.apiResponse import ApiResponse


class ProductInStores:

	def get(product):
		"""
		"""
		productInStores = ProductInStore.objects.filter(product__name=product)
		data = ProductInStoreSerializer(productInStores, many=True).data
		res = ApiResponse(success=True, message="Successfully retrieved stores", data=data)
		return res

	def putPromotion(retailStore, product, promotion):
		"""
		"""
		status = ProductInStore.objects.filter(retailStore__name=retailStore, product__name=product).update(promotion=promotion)
		res = ApiResponse(success=True, message="Successfully updated promotion")
		return res


