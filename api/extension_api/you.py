import pyyoutube
import json

api = pyyoutube.Api(api_key="AIzaSyC1MdrF1pr0_GSXutgMdqDNsPhr8DujyeI")
# print(api.get_comment_threads(video_id="rvIZjhj8M50",return_json=True))
comment_list = api.get_comment_threads(video_id="rvIZjhj8M50",return_json=False,limit=100,count=None)
for i in comment_list.items:
    print(i.snippet.topLevelComment.snippet.textDisplay)