from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.http import require_POST

from .forms import ViewerSignUpForm
from .models import User
from .tokens import account_activation_token


def viewer_signup(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    
    if request.method == 'POST':
        form = ViewerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # User shouldn't log in before confirming email
            user.is_active = False
            user.is_viewer = True
            user.save()
            current_site = get_current_site(request)

            if request.is_secure():
                protocol = 'https'
            else:
                protocol = 'http'
            
            subject = render_to_string(
                'registration/account_activation_subject.txt', 
                {'site_name': current_site.name}
            )
            
            message = render_to_string(
                'registration/account_activation_email.html',
                {'user': user,
                 'domain': current_site.domain,
                 'protocol': protocol,
                 'site_name': current_site.name,
                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                 'token': account_activation_token.make_token(user),}
            )
            user.email_user(subject, message)
            return redirect('accounts:account_activation_sent')
        else:
            messages.error(request, "An error occured while trying to create your account.")
            return render(request,
                'registration/signup.html',
                {'form': form})
    else:
        form = ViewerSignUpForm()

    template = 'registration/signup.html'
    context = {
        'form': form
    }
    
    return render(request, template, context)


def account_activation_sent(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    template = 'registration/account_activation_sent.html'
    context = {}

    return render(request, template, context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_verified = True
        user.save()
        login(request, user, backend='accounts.authentication.EmailAuthBackend')
        messages.success(request, 'Your profile has been successully created.')
        return redirect('core:home')
    else:
        return render(
            request,
            'registration/activate.html',
            {})
  

def password_reset_options(request):

    template = 'registration/password_reset_options.html'
    context = {}

    return render(request, template, context)
