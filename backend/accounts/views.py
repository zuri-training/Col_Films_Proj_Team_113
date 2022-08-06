from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from . models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, get_user_model, logout
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from .decorators import ajax_required

=from .forms import SignUpForm, UserForm, =ResendActivationEmailForm
from .tokens import account_activation_token
from .models import Profile, Follow



def homepage(request):
	User = CustomUser.objects.all() #queryset containing all books we just created
	return render(request=request, template_name="main/home.html", context={'user':User})


def signup(request):
    if request.user.is_authenticated():
        return redirect('home')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # User shouldn't log in before confirming email
            user.is_active = False
            user.save()
            # Load profile instance created by the signal
            user.refresh_from_db()
            user.profile.favorite_club = form.cleaned_data.get('favorite_club')
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
            return redirect('account_activation_sent')
        else:
            messages.error(request, "An error occured while trying to create your account.")
            return render(request,
                'registration/signup.html',
                {'form': form})
    else:
        form = SignUpForm()

    template = 'registration/signup.html'
    context = {
        'form': form
    }
    
    return render(request, template, context)


def account_activation_sent(request):
    if request.user.is_authenticated():
        return redirect('home')

    template = 'registration/account_activation_sent.html'
    context = {}

    return render(request, template, context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        messages.success(request, 'Your profile has been successully created.')
        return redirect('home')
    else:
        return render(
            request,
            'registration/activate.html',
            {})

# #Register
# def register_request(request):
#     if request.method == "POST":
#       form = NewUserForm(request.POST)
#       if form.is_valid():
#         user = form.save()
#         login(request, user)
        
#         messages.success(request, "Registration successful." )
#         return redirect("main:homepage")
#       messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render (request=request, template_name="main/register.html", context={"register_form":form})
  
# #Login 
# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("main:homepage")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="main/login.html", context={"login_form":form})





# #Logout
# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("main:homepage")
