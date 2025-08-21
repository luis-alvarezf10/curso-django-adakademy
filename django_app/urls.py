from django.urls import path
from .views import PostView 

urlpatterns = [
    # Agrega aquí tus URLs específicas de la app
    path('', PostView.as_view(), name='post'),
]