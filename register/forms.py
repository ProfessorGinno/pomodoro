from django.forms import ModelForm
from .models import User
# from django.contrib.auth.models import User

class NewUser(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]