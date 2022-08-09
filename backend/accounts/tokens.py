from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


# Extend the PasswordResetTokenGenerator to create a 
# unique token generator to confirm email addresses. 
# This make use of the project's SECRET_KEY 

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.email_verified)
        )

account_activation_token = AccountActivationTokenGenerator()
