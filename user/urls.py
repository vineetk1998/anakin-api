from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from app.middlewares import login_exempt
from user import views
# from . import views

urlpatterns = [
    path("login", login_exempt(csrf_exempt(views.LoginView.as_view())), name="login"),
    path("user", login_exempt(csrf_exempt(views.UserView.as_view())), name="user")
]