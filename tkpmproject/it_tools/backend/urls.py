from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name="logout"),
    path('', views.it_tools, name="it_tools"),
    path('api/user/<int:user_id>/go_premium/', views.go_premium, name="go_premium")
]