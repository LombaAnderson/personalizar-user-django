from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    
    # user management
    path('accounts/', include('allauth.urls')),    
   
    # local
    path("", include("pages.urls", namespace="pages")),
]
