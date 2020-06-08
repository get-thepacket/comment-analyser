from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .library.naive import loader
import json

from pyyoutube
# Create your views here.
def index(request):
    api = pyyoutube.Api(api_key='AIzaSyC1MdrF1pr0_GSXutgMdqDNsPhr8DujyeI')
    if request.method == "GET":
        return HttpResponse('API loaded in api/')
    if request.method == "POST":
        json_data = json.loads(request.body.decode('utf-8'))
        score=0
        
        comment_list = api.get_comment_threads(video_id=json_data.link,limit=100,count=None)
        list_comment = []
        for i in comment_list.items:
            list_comment.append(i.snippet.topLevelComment.snippet.textDisplay)
        
        score+=loader(list_comment)
        result=""
        if score>0:
            result = "Positive"
        else result = "Negative"
        send_data = {
            "sent_id" : json_data.link,
            "prediction" : result
        }
        return JsonResponse(send_data)



