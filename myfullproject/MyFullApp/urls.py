from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('product/',views.Product,name='product'),
    path('about/',views.about,name='about'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:bag>',views.category,name='category'),

]