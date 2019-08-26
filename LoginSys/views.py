# -*- coding utf-8 -*-

from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from LoginSys.models import ProfessionalRegistrationForm
from django.core.mail import EmailMessage
from Profession import settings
from django.contrib.auth.models import User
from Profile.models import Profile
import random
import string

# Create your views here.


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            try:
                User.objects.get(username=username)
                args['login_error'] = "Пользователь не активирован"
                return render_to_response('login.html', args)
            except:
                args['login_error'] = "Пользователь не найден"
                return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def generate_string(size=24, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def send_verification_message(username, email):
    subject = "Подтверждение регистрации"
    salt = generate_string(24)
    verification_link = "http://127.0.0.1:8000/activate_user/" + username + "/" + salt
    message = "Вы зарегестрировались на сайте, для завершения регистрации перейдите по ссылке: " + verification_link
    recipients = [email]
    msg = EmailMessage(subject, message,
                       from_email=settings.EMAIL_HOST_USER,
                       to=recipients,)
    msg.content_subtype = 'html'
    msg.send(fail_silently=True)
    return salt


def registration(request):
    args = {}
    args.update(csrf(request))
    args['user_creation_form'] = ProfessionalRegistrationForm()
    if request.POST:
        new_user_form = ProfessionalRegistrationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password2'],
                                         email=new_user_form.cleaned_data['email'],)
            salt = send_verification_message(new_user.username, new_user.email)
            new_user.profile.activation_salt = salt
            new_user.is_active = False
            new_user.save()
            auth.login(request, new_user)
            return render_to_response('AccountActivation.html')
        else:
            args['user_creation_form'] = new_user_form
    return render_to_response('registration.html', args)


def personal_account(request):
    return render_to_response("../PersonalAccount/templates/PersonalAccount.html")


def personal_tests(request):
    return render_to_response("../PersonalAccount/templates/PersonalTests.html")
