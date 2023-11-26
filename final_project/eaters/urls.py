from django.urls import path
from . import views
from .views import home,eaters,cart,restaurant,login,checkout,update_menu,add_menu,delete_menu,search_results,CustomLoginView



urlpatterns = [
  path('', views.home, name='home'),
  path ('eaters/', views.eaters, name='eaters'),
  path('cart/', views.cart, name='cart'),
  path('restaurant/', views.restaurant, name='restaurant'),
  path('login/', CustomLoginView.as_view(), name='login'),
  # path('login/', views.login, name='login'),
  path('checkout/', views.checkout, name='checkout'),
  path('update_menu/<int:pk>/', views.update_menu, name='update_menu'),
  path('add_menu/', views.add_menu, name='add_menu'),
  path('delete_menu/<int:pk>/', delete_menu, name='delete_menu'),
  path('search_results/', search_results, name='search_results'),

 
  
  
 
]
