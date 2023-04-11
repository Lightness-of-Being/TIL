from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class meta(UserCreationForm):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):

    class meta(UserChangeForm):
        model = get_user_model()