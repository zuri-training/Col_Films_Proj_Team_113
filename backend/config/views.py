# from contextlib import redirect_stderr
# from distutils.command.upload import upload
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.db.models import Case, When

# from .models import WatchLater, Video
# # Create your views here.

# # def videos()   
# # def uploads ## If there was an existing function for the video n upload

# def watchlater(request):
#     if request.method == "POST":
#         user = request.user.username
#         video_id = request.POST('video_id')
        
#         watch = WatchLater.objects.filter(user=user)
        
#         for i in watch:
#             if video_id == video_id:
#                 message = "Your video is already added"
#                 break
#         else:         
#             watchlater = WatchLater(user=user, video_id= video_id)
#             watchlater.save()
#             message ="Your video has been added"
        
#         # where Video is model that rep the videos uploaded 
#         video = Video.objects.filter(watch_id = video_id).first()
#         return redirect("videos/videopost.html", {'video' : video, "message": message})
    
    
#     wl = WatchLater.objects.filter(user=request.user)
#     ids = []
    
#     for i in wl:
#         ids.append(i.video_id)
    
#     # persuse and content are random var.  
#     peruse = Case(*[When(pk=pk,then=pos) for pos, pk in enumerate(ids)])
#     content = WatchLater.objects.filter(content_id__in= ids).order_by(peruse)
        
#     template = 'videos/watchlater.html'
    
#     return render(request, template, {'content': content})
    
    