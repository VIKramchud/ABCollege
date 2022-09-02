"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from graduates import views
from ABcollegE import views


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
   # path('accounts/',include('accounts.urls')),
    path("index/", views.index, name="index"),
    path("register/", views.register, name="register"),
    path('',views.home),
    path('about/',views.about),
    path('index/index',views.index),
    #path("login",views.login),
    path('internship/',views.internship),
    path('register/register',views.register, name='register'),
    path('galgotias/',views.galgotias),
    path('logout/',views.logout),
    path('intern/',views.intern),
    path('intern/internform/',views.internform),
    path('search/',views.search),
    path('lms/',views.lms),
    path('notes/',views.notes),
    path('scholarform/',views.scholarform),
    path('successscholar1/',views.successscholar1),
    
    path('successintern1/',views.successintern1),

    path('events/',views.events),

    #path('register/',views.register, name='register'),
  #  path('',views.first),
   # path('login/',views.login),
   # path('second/',views.second),
   # path('second/add',views.add, name='add'),
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += staticfiles_urlpatterns()

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)