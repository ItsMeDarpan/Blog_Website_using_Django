
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('main.urls')),
    path('', include('main.urls')),
]
