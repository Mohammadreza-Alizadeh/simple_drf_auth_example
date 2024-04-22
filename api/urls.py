from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='UserRegisterView'),
    path('login/', views.UserLoginView.as_view(), name='UserLoginView'),
    path('check/', views.CheckAuthenticationView.as_view(), name='CheckAuthenticationView')

]
