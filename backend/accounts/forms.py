from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

USERNAME_REGEX = '^[a-zA-Z0-9]*$'

DISALLOWED_USERNAMES = [
	'activate', 'account', 'admin', 'about', 'administrator', 'activity', 'account', 'auth', 'authentication',
	'blogs', 'blog', 'billing', 
	'create', 'cookie', 'contact', 'config', 'contribute', 'campaign',
	'disable', 'delete', 'download', 'downloads', 'delete',
	'edit', 'explore', 'email', 
	'footystory', 'follow', 'feed', 'forum', 'forums',
	'intranet',
	'jobs', 'join',
	'login', 'logout', 'library',
	'media', 'mail', 
	'news', 'newsletter',
	'help', 'home', 
	'privacy', 'profile',
	'registration', 'register', 'remove', 'root', 'reviews', 'review',
	'signin', 'signup', 'signout', 'settings', 'setting', 'static', 'support', 'status', 'search', 'subscribe', 'shop',
	'terms', 'term',
	'update', 'username', 'user', 'users', 
]


class SignUpForm(UserCreationForm):
	username = forms.CharField(
		max_length=150,
		validators=[RegexValidator(
			regex=USERNAME_REGEX,
			message="Your username contains invalid characters.",
			code='invalid_username' )],
		help_text='Username must be alphanumeric only.',
		required=True)
	email = forms.EmailField(
		max_length=254,
		required=True,
		help_text='Enter a valid email address.')

	class Meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']

	def clean_username(self):
		username = self.cleaned_data.get('username').lower()
		if username in DISALLOWED_USERNAMES:
			raise forms.ValidationError("You are not allowed to make use of this username.")
		if len(username) < 4:
			raise forms.ValidationError("Your username must not be less than 4 (four) characters.")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email__iexact=email).exists():
			raise forms.ValidationError("A user with that email already exists.")
		return email

# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user
