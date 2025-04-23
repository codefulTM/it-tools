from django.urls import path
from . import views

urlpatterns = [
    path('category/6/qr-code-generator/', views.qr_code_generator_tool, name='qr_code_generator'),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name='logout'),
    path('', views.it_tools, name="it_tools")
]