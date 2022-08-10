from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class SignUpForm(UserCreationForm):
	# username = forms.CharField(
	# 	max_length=150,
	# 	validators=[RegexValidator(
	# 		regex=USERNAME_REGEX,
	# 		message="Your username contains invalid characters.",
	# 		code='invalid_username' )],
	# 	help_text='Username must be alphanumeric only.',
	# 	required=True)
	# email = forms.EmailField(
	# 	max_length=254,
	# 	required=True,
	# 	help_text='Enter a valid email address.')

	class Meta:
		model = User 
		fields = ['email', 'password1', 'password2']

	# def clean_username(self):
	# 	username = self.cleaned_data.get('username').lower()
	# 	if username in DISALLOWED_USERNAMES:
	# 		raise forms.ValidationError("You are not allowed to make use of this username.")
	# 	if len(username) < 4:
	# 		raise forms.ValidationError("Your username must not be less than 4 (four) characters.")
	# 	return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email__iexact=email).exists():
			raise forms.ValidationError("A user with that email already exists.")
		return email

class ViewerSignUpForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2']

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_viewer = True
    #     user.save()
    #     return user

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
