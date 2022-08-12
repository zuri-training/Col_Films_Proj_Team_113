from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmailAuthBackend(BaseBackend):
    """Authenticate using e-mail address."""

    def authenticate(self, request, username=None, password=None):
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
