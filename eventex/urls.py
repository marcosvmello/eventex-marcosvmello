from django.contrib import admin
from django.urls import path, include

from eventex.core.views import home, speaker_detail

urlpatterns = [
    path('', home, name='home'),
    path('inscricao/', include('eventex.subscriptions.urls')),
    path('palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]
