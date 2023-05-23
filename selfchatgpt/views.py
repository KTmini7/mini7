from django.shortcuts import render
import openai
from mysite import settings
# Create your views here.
openai.api_key = settings.SECRET_KEY


#chatGPT에게 채팅 요청 API
def chatGPT(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    print(completion)
    result = completion.choices[0].message.content
    return result

#chatGPT에게 그림 요청 API
def imageGPT(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    result =response['data'][0]['url']
    return result

def index(request):
    return render(request, 'selfgpt/index.html')

def chat(request):
    #post로 받은 question
    prompt = request.POST.get('question')


    #type가 text면 chatGPT에게 채팅 요청 , type가 image면 imageGPT에게 채팅 요청
    result = chatGPT(prompt)

    context = {
        'question': prompt,
        'result': result
    }

    return render(request, 'selfgpt/result.html', context) 