from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class SignupForm(UserCreationForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_MARITAL_STATUS = (
        (None, '-- Select your marital status --'),
        ('Single', 'Single'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced')
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'mb-2'}), required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'type': 'email', 'class': 'mb-2'}), required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER, required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), required=True)
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_MARITAL_STATUS, required=True)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'dob', 'gender', 'phone_no', 'marital_status', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_MARITAL_STATUS = (
        (None, '-- Select your marital status --'),
        ('Single', 'Single'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced')
    )

    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER, required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), required=True)
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_MARITAL_STATUS, required=True)

    class Meta:
        model = User
        fields = ['dob', 'gender', 'phone_no', 'marital_status', 'profile_pic']


class EditProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SELECT_MARITAL_STATUS = (
        (None, '-- Select your marital status --'),
        ('Single', 'Single'),
        ('Engaged', 'Engaged'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced')
    )

    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'mb-2'}), disabled=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_GENDER, disabled=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'mb-2'}), required=True)
    marital_status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_MARITAL_STATUS, required=True)

    class Meta:
        model = User
        fields = ['dob', 'gender', 'phone_no', 'marital_status', 'profile_pic']
