from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def project1(request):
    return render(request,'project1.html')


def project2(request):
    return render(request,'project2.html')


def team(request):
    return render(request,'team.html')

def model(request):
    return render(request,'model.html')

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('chatgpt/',include('chatgpt.urls')),
    path('signlanguagetochatgpt/',include('signlanguagetochatgpt.urls')),
    path('selfchatgpt/', include('selfchatgpt.urls')),
    path('selfsignlanguagetochatgpt/', include('selfsignlanguagetochatgpt.urls')),
    path('project1/', project1),
    path('project2/',project2),
    path('team/', team),
    path('model/',model),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)