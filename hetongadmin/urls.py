"""hetongadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin


from login import views as login
from contract import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login.Login),
    url(r'^login/', login.Login),
    url(r'^index/', login.Index),
    url(r'^contract/', views.Contract_info_add),
    url(r'^table/getpage', views.Getpage),
    url(r'^table/delete', views.Delete),
    url(r'^table/search', views.Search),
    url(r'^table/update', views.Update),
    url(r'^table/', views.Contract_tables),

    #url(r'^login/',include('login.urls')),
    #url(r'^static/',include('login.urls'))
]
