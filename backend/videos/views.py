from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from core.utils import mk_paginator
from django.utils.text import slugify
from django.contrib import messages
from moviepy.editor import VideoFileClip
from django.core.files.uploadedfile import UploadedFile
from .forms import VideoUploadForm, CommentForm
from .models import Video, Category


# def video_list(request, category_slug=None):
#     categories = Category.objects.all()
#     category = None
#     products = Product.objects.filter(is_available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = category.products.filter(is_available=True)
#     product_count = products.count()
#     products = mk_paginator(request, products, 3)

#     template_name = "products/list.html"
#     context = {
#         "products": products,
#         "categories": categories,
#         "category": category,
#         "product_count": product_count,
#     }

#     return render(request, template_name, context)

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


# def product_update(request, id):
#     """ View to enable a Vendor update a product. """
#     product = get_object_or_404(Product, id=id, vendor=request.user)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, "Your product has been successfully updated.")
#             return redirect(product)
#     else:
#         form = ProductForm(instance=product)

#     template_name = "products/form.html"
#     context = {
#         'form': form,
#     }

#     return render(request, template_name, context)


# def product_delete(request, id):
#     # Use a Modal instead?
#     product = get_object_or_404(Product, id=id, vendor=request.user)
#     if request.method == 'POST':
#         product.delete()
#         messages.success(
#             request, "Your product has been deleted.")
#         return redirect(product)

#     template_name = "products/delete.html"
#     context = {
#         'product': product,
#     }

#     return render(request, template_name, context)


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
    }

    return render(request, template, context)
