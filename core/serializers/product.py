from rest_framework import serializers
from core.models import Product

class ProductSerializer(serializers.ModelSerializer):

	brand = serializers.SerializerMethodField()

	def get_brand(self, obj):
		return obj.brand.name

	class Meta:
		model = Product
		fields = [
			"name",
			"brand"
		]