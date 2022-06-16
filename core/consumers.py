import json
import logging
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
logger = logging.getLogger(__name__)

class NotificationConsumer(WebsocketConsumer):
	def connect(self):
		self.room_group_name = "notification"

		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
			)

		self.accept()

		self.send(text_data=json.dumps({
			'type': 'connection_established',
			'message': 'You are now connected!'
			}))

	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		print(message)

		# someOutsideFunc()

		# async_to_sync(self.channel_layer.group_send)(
		# 	self.room_group_name,
		# 	{
		# 		'type': 'chat_message',
		# 		'message': message
		# 	}
		# )

	def chat_message(self, event):
		data = event['data']
		self.send(text_data=json.dumps({
			'type': 'notification',
			'message': "Price Drop", 
			'data': data
			}))


	@staticmethod
	def sendNotification(data):
		logger.info("Sending notification")
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
			'notification',
			{'type': 'chat_message', 'data': data}
		)


