from django.urls import path
from .views import views_authentication
from .views import views_main_page
from .views import views_admin_page

urlpatterns = [
    path('login/', views_authentication.login, name="login"),
    path('signup/', views_authentication.signup, name="signup"),
    path('logout/', views_authentication.logout, name='logout'),
    path('managetools/', views_admin_page.manage_tools, name="manage_tools"),
    path('addtool/', views_admin_page.add_tool, name="add_tool"),
    path('tools/<int:tool_id>/', views_main_page.use_tool, name="use_tool"),
    path('', views_main_page.it_tools, name="it_tools")
]