"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from todolist.views import index, page2, page3, show_week_targets
from django.urls import path

#from . import views #index, page2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="TodoList"),
#    url('page2/', page2,name="webpage2"),
    url('show_week_targets/', show_week_targets,name="webpage_show_week_targets"),
    url('page2/', page2, name="webpage2"),
    url('page3/', page3, name="webpage3"),
#    url('page4/', page4, name="webpage4"),
#    path('page2',index.webpage2,name="webpage2"),
]

#    path('', views.post_list, name='post_list'),     
#    path('post/new/', views.post_new, name='post_new'), 
#    path('post/<int:pk>/', views.post_detail, name='post_detail'),     
#    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),