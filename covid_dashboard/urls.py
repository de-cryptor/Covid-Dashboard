"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app.views import Home,Vaccination,Oxygen,Plasma,Beds,Remdesivir,Donation,Guidelines,CaseTracker


urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('vaccination/', Home.as_view(),name='vaccination'),
    path('oxygen/', Home.as_view(),name='oxygen'),
    path('plasma/', Home.as_view(),name='plasma'),
    path('beds/', Home.as_view(),name='beds'),
    path('remdesivir/', Home.as_view(),name='remdesivir'),
    path('donation/', Home.as_view(),name='donation'),
    path('guidelines/', Home.as_view(),name='guidelines'),
    path('case-tracker/', Home.as_view(),name='case-tracker'),
    path('admin/', admin.site.urls),
    # path('dashboard/', include('app.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
