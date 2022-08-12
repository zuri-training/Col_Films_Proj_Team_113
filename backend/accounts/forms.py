from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CreatorSignUpForm(UserCreationForm):

	class Meta:
		model = User 
		fields = ['email', 'password1', 'password2']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email__iexact=email).exists():
			raise forms.ValidationError("A user with that email already exists.")
		return email

class ViewerSignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2']
