from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django.utils.translation import gettext_lazy as _

User = get_user_model()


# def validate_school_email(email):
#     """Verifies that the email has a .edu extension."""
#     if ".edu" not in email.split("@")[1]:
#         raise forms.ValidationError("Your email has to be a school email.")
#     else:
#         return email


class CreatorSignUpForm(UserCreationForm):
    document = forms.ImageField(required=True)
    class Meta:
        model = User 
        fields = ['email', 'password1', 'password2', 'document']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        if ".edu" not in email.split("@")[1]:
            raise forms.ValidationError("Your email has to be a school email.")
        return email

class ViewerSignUpForm(UserCreationForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.visible_fields():
    #         field.field.help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
