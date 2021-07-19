from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import Authors

class UserExtendForm(UserCreationForm):
    organization = forms.CharField(max_length=120)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'organization', 'password1', 'password2']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserExtendForm, self).save(commit=True)
        user_profile = Authors(user=user, organization=self.cleaned_data['organization'])
        print(user_profile)
        user_profile.save()
        return user, user_profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
