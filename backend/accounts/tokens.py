import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    Extend the PasswordResetTokenGenerator which makes use of the project's SECRET_KEY
    to create a unique token generator to confirm email addresses.
    """
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.email_verified)
        )

account_activation_token = AccountActivationTokenGenerator()
