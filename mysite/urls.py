from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
import openai

def index(request):
    return render(request,'index.html')

def project1(request):
    return render(request,'project1.html')


def project2(request):
    return render(request,'project2.html')

def chatGPT(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    print(completion)
    result = completion.choices[0].message.content
    return result

def project1_result(request):
    #post로 받은 question
    prompt = request.POST.get('question')


    #type가 text면 chatGPT에게 채팅 요청 , type가 image면 imageGPT에게 채팅 요청
    result = chatGPT(prompt)

    context = {
        'question': prompt,
        'result': result
    }

    return render(request,'project1_result.html', context) 

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
    path('project1_result',project1_result),
    path('project2/',project2),
    path('team/', team),
    path('model/',model),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)