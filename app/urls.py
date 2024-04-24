from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('u/<str:user>', views.anonymous, name='anonymous'),
    path('delete-feedback/<uuid:comment>', views.deleteFeedback, name='delete-feedback'),
]

