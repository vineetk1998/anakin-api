from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from app.middlewares import login_exempt
from core import views

urlpatterns = [
    path("product", login_exempt(csrf_exempt(views.ProductView.as_view())), name="product"),
    path("retailStore", login_exempt(csrf_exempt(views.ProductInStoreView.as_view())), name="retailStore"),
    path("promotion", login_exempt(csrf_exempt(views.PromotionView.as_view())), name="promotion")
]