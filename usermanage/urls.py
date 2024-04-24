from django.urls import path
from usermanage import views

urlpatterns = [
    path('sign-in/', views.signIn, name='sign-in'),
    path('sign-up/', views.signUp, name='sign-up'),
    path('logout/', views.logoutHandle, name='logout'),
]
