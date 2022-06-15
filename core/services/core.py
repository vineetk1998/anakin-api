# from core.serializers import RetailStoreSerializer
# from core.models import RetailStore

# class RetailStore:
# 	def get(product, offset, limit):
# 		"""
# 		"""
# 		retailStores = RetailStore.objects.all()[offset:limit]
# 		data = RetailStoreSerializer(retailStores, many=True).data
# 		res = ApiResponse(success=True, message="Successfully retrieved products", data=data)
# 		return res
