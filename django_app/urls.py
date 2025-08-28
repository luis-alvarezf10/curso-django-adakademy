from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', PostView.as_view(),name = 'post'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

