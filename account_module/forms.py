from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(4)
        ]
    )
    confirm_password = forms.CharField(
        label='تایید رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تایید رمزعبور'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(4)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        # if password == confirm_password:
        #     return confirm_password
        # raise ValidationError('رمز ورود و تکرار آن یکسان نیستند')
        if password != confirm_password:
            raise ValidationError('رمز ورود و تکرار آن یکسان نیستند')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(4)
        ]
    )



class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(4)
        ]
    )
    confirm_password = forms.CharField(
        label='تایید رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تایید رمزعبور'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(4)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('رمز ورود و تکرار آن یکسان نیستند')