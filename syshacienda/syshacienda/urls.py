"""syshacienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from baseapp import urls
from mnt import urls
from vent import urls
from api import urls

urlpatterns = [
    path('', include(('baseapp.urls','baseapp'), namespace="baseapp")),
    path('mnt/', include(('mnt.urls','mnt'), namespace="mnt")),
    path('vent/', include(('vent.urls','vent'), namespace="vent")),
    path('api/', include(('api.urls','api'), namespace="api")),
    path('rpts/', include(('rpts.urls','rpts'), namespace="rpts")),
    path('admin',admin.site.urls),

]

admin.site.site_header = 'Panel de control de Administración de Hacienda'
admin.site.index_title = 'ADMINISTRACIÓN DEL SISTEMA'
#admin.site.site_title = 'SysAdmin'
 # 
