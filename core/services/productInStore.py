import logging
from core.serializers import ProductInStoreSerializer
from core.models import ProductInStore
from utils.apiResponse import ApiResponse
from core.consumers import NotificationConsumer
logger = logging.getLogger(__name__)


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
		try:
			intPromotion = int(promotion)
		except:
			res = ApiResponse(message="Promotion should be an integer value")
			return res

		logger.info("Updating promotion")

		productInStores = ProductInStore.objects.filter(retailStore__name=retailStore, product__name=product)
		logger.info("Updating adfadf")
		try:
			logger.info(productInStores.count())
			if productInStores.count():
				productInStore = productInStores[0]
				logger.info("check if higher discount")
				if (productInStore.promotion and int(productInStore.promotion) < intPromotion) or not productInStore.promotion:
					data = ProductInStoreSerializer(productInStore).data
					NotificationConsumer.sendNotification(data)
		except Exception as ex:
			logger.error("Error in sending notification %s", str(ex))
			productInStores.update(promotion=promotion)

		res = ApiResponse(success=True, message="Successfully updated promotion")
		return res

