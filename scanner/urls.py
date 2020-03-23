from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('selector/', views.selector, name='selector'),
    path('selector/loader/', views.model_img, name='image'),
    path('success', views.success, name='success'),
    path('selector/speech/', views.speech_to_text, name='speech'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
