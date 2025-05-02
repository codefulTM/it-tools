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
    path('enableanddisabletool/', views_admin_page.enable_and_disable_tool, name="enable_and_disable_tool"),
    path('togglepremium/', views_admin_page.toggle_premium_tool, name="toggle_premium_tool"),
    path('removetool/', views_admin_page.remove_tool, name="remove_tool"),
    path('tools/<int:tool_id>/', views_main_page.use_tool, name="use_tool"),
    path('categories/<int:category_id>/', views_main_page.it_tools_by_category, name="get_tools_by_category"),
    path('', views_main_page.it_tools, name="it_tools")
]