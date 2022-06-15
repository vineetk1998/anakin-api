from rest_framework import serializers
from core.models import ProductInStore

class ProductInStoreSerializer(serializers.ModelSerializer):

	retailStore = serializers.SerializerMethodField()
	product = serializers.SerializerMethodField()
	# retailer = serializers.SerializerMethodField()

	def get_retailStore(self, obj):
		return obj.retailStore.name

	def get_product(self, obj):
		return obj.product.name

	class Meta:
		model = ProductInStore
		fields = [
			"retailStore", 
			"product",
			"promotion",
			"available"
		]