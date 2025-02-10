from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
<<<<<<< HEAD
from .models import UserProfile
=======
from .models import UserProfile, CustomUser
>>>>>>> 9727532 (Hatola hali kop)


class SignupForm(UserCreationForm):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
=======
        fields = ('email', 'password1')
>>>>>>> 9727532 (Hatola hali kop)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'})


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
<<<<<<< HEAD
                'class': 'block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter Email',
=======
                "id": "email",
                "name": "email",
                "type": "email",
                "required": True,
                'placeholder': "name@school.com",
                'class': 'block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
>>>>>>> 9727532 (Hatola hali kop)
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
<<<<<<< HEAD
                'class': 'block w-full pl-10 pr-10 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter your password',
=======
                "id": "password",
                "name": "password",
                'placeholder': 'Enter your password',
                'class': 'block w-full pl-10 pr-10 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
>>>>>>> 9727532 (Hatola hali kop)
            }
        )
    )
    remember_me = forms.BooleanField(required=False)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'dob', 'phone_number']