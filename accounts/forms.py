from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# forms.py
# How would Users be created in our program? When a user creates a new account and when an admin creates an account.


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        """ For both new forms, we are using the Meta class to override the default fields by setting the
            model to our CustomUser and using the default fields via Meta.fields which includes all default
            fields. To add our custom age field, we simply tack it on at the end, and it will display automatically
            on our future signup page.

        If you want to add more fields of information for your signup sheet to collect
        than you need to update the field names. 
        """
        fields = UserCreationForm.Meta.fields + (
            "username",
            "email",
            "age",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )
