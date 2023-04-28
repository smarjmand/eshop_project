from django.shortcuts import render, redirect
from django.views import View
from account_module.forms import RegisterForm, LoginForm
from account_module.forms import ForgotPasswordForm, ResetPasswordForm
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404
from django.contrib.auth import login








class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_password = register_form.cleaned_data.get('password')
            user_email = register_form.cleaned_data.get('email')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'این ایمیل تکراری است!')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email
                )
                new_user.set_password(user_password)
                new_user.save()
                # todo : send active code to user email-account
                return redirect('home_page')
        return render(request, 'register.html', {'register_form': register_form})


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo : show success message to user
                return redirect('login_page')
            else:
                # todo : show the account is active already to user
                pass
        raise Http404



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'login_form': LoginForm()})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect('home_page')
                    else:
                        login_form.add_error('email', 'پسورد وارد شده صحیح نیست')
            else:
                login_form.add_error('email', 'کاربری با این مشخصات یافت نشد')
        return render(request, 'login.html', {'login_form': login_form})


class ForgetPassword(View):
    def get(self, request):
        recovery_form = ForgotPasswordForm()
        return render(request, 'forget_password.html', {'recovery_form': recovery_form})

    def post(self, request):
        recovery_form = ForgotPasswordForm(request.POST)
        if recovery_form.is_valid():
            user_email = recovery_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                # todo: send reset-password email to user
                pass


        recovery_form = ForgotPasswordForm()
        return render(request, 'forget_password.html', {'recovery_form': recovery_form})

#-------------------------------------------------

class ResetPassword(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect('login_page')

        reset_pass_form = ResetPasswordForm()
        return render(request, 'reset_password.html', {'reset_pass_form': reset_pass_form})