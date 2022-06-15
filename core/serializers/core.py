from rest_framework import serializers
from core.models import RetailStore

class RetailStoreSerializer(serializers.ModelSerializer):

	class Meta:
		model = RetailStore
		fields = [
			'name',
		]