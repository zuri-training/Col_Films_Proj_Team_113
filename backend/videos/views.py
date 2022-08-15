from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from core.utils import mk_paginator
from django.utils.text import slugify
from django.contrib import messages
from moviepy.editor import VideoFileClip
from .forms import VideoUploadForm, CommentForm
from django.http import HttpResponseBadRequest
from .models import Video, Category



def format_video_length(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return f'{mins}:{seconds}'

@login_required
def video_create(request):
    """
    View to enable a Creator upload a video.

    Template: ``videos/video_create.html``
    Context:
        form
            Video form
    """
    if not request.user.is_creator:
        messages.success(
            request, 'Only creators are allowed to upload a video.')
        return redirect('core:home')
    
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.slug = slugify(video.title)
            
            video_file_path = request.FILES['video_file']
            clip = VideoFileClip(video_file_path.temporary_file_path())
            temporary_video_length = int(clip.duration)
            if temporary_video_length > 900:
                video_length_error = 'Your video was more than 15 minutes, upload another.'
                return render(
                    request, 'videos/video_create.html',
                    {'form':form, 'video_length_error': video_length_error})
            elif temporary_video_length <= 900:
                video.video_length = format_video_length(int(clip.duration))
                video.save()
                return redirect(video.get_absolute_url())
        else:
            messages.warning(
                request, "An error occured, check below.") 
    else:
        form = VideoUploadForm()

    template = 'videos/video_create.html'
    context = {
        'form': form,
        'categories': categories,
    }

    return render(request, template, context)


@login_required
def video_detail(request, slug):
    """
    Video detail.

    Template: ``videos/video_detail.html``
    Context:
        video
            Given video
    """

    video = get_object_or_404(Video, slug__iexact=slug)

    session_key = 'viewed_story_{}'.format(video.pk)
    if not request.session.get(session_key, False):
        video.impressions += 1
        video.save()
        request.session[session_key] = True

    similar_videos = Video.objects.filter(
        category=video.category).exclude(id=video.id)

    comments = video.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.video = video
            comment.save()
            messages.success(
                request, "Thanks! Your comment was submitted successfully.")
            return redirect(video.get_absolute_url())
        else:
            messages.warning(
                request, "An error occured while submitting your form, check below")
    else:
        comment_form = CommentForm()


    template = 'videos/video_detail.html'
    context = {
        'video': video,
        'similar_videos': similar_videos,
        'comments': comments,
    }

    return render(request, template, context)


@login_required
def video_favorite(request, id):
    video = get_object_or_404(Video, id=id)
    current_url = request.META['HTTP_REFERER']
    users_favorites = video.users_favorites.filter(
        email=request.user.email)
    if not users_favorites:
        video.favorites += 1
        video.users_favorites.add(request.user)
        messages.success(
            request, "This video has been added to your favorites.")
        return redirect(current_url)
    else:
        return HttpResponseBadRequest()


@login_required
def video_unfavorite(request, id):
    video = get_object_or_404(Video, id=id)
    current_url = request.META['HTTP_REFERER']
    users_favorites = video.users_favorites.filter(
        email=request.user.email)
    if users_favorites:
        video.favorites -= 1
        video.users_favorites.remove(request.user)
        messages.success(
            request, "This video has been deleted from your favorites.")
        return redirect(current_url)
    else:
        return HttpResponseBadRequest()
