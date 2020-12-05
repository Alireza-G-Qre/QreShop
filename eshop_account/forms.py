from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد کنید'}),
        label='کلمه عبور'
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        is_user = User.objects.filter(username=username).exists()
        if not is_user:
            raise forms.ValidationError('کاربری با این نام یافت نشد')
        return username


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(limit_value=20, message='تعداد کاراکترهانمیتواند بیشتر از 20 باشد'),
            validators.MinLengthValidator(8, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه ی عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا تکرار کلمه عبور خود را وارد نمایید'}),
        label='تکرار کلمه ی عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')

        if len(email) > 200:
            raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 200 باشد')

        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_user_by_username = User.objects.filter(username=username).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')

        return username

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password
