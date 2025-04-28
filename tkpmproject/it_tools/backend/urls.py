from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name='logout'),
    path('managetools/', views.manage_tools, name="manage_tool"),
    path('addtool/', views.add_tool, name="add_tool"),
    path('', views.it_tools, name="it_tools")
]