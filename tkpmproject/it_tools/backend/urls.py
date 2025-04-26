from django.urls import path
from . import views

urlpatterns = [
    path('category/6/qr-code-generator/', views.qr_code_generator_tool, name='qr_code_generator'),
    path('category/6/wifi-qr-code-generator/', views.wifi_qr_code_generator_tool, name='wifi_qr_code_generator'),
    path('category/6/svg-placeholder-generator', views.svg_placeholder_generator_tool, name='svg_placeholder_generator'),
    path('category/7/random-prime-generator', views.random_prime_generator_tool, name='random_prime_generator'),
    path('category/7/random-name-generator', views.random_name_generator_tool, name='random_name_generator'),
    path('category/7/random-date-generator', views.random_date_generator_tool, name='random_date_generator'),
    path('category/8/text-difference-checker', views.text_difference_checker_tool, name='text_difference_checker'),
    path('category/8/text-statistics', views.text_statistics_tool, name='text_statistics'),
    path('category/8/lorem-ipsum-generator', views.lorem_ipsum_generator_tool, name='lorem_ipsum_generator'),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name='logout'),
    path('', views.it_tools, name="it_tools")
]