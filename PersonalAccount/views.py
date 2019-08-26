from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from Test.models import Test, UsersAnswers, Results
from Profile.models import Profile
from django.template.context_processors import csrf
# Create your views here.


def reset_answers(request):
    user = auth.get_user(request)
    answers = UsersAnswers.objects.filter(user=user)
    for answer in answers:
        answer.delete()
    results = Results.objects.filter(user_id=user)
    for result in results:
        result.delete()
    user.profile.reset_test()
    return redirect("personal_tests/")


def activate_user(request, current_login="Login", activation_salt="yeap"):
    user = User.objects.get(username=current_login)
    salt = user.profile.activation_salt
    if salt == activation_salt:
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("/")
    else:
        return render_to_response("AccountActivation.html")


def personal_account(request):
    user = User.objects.get(id=auth.get_user(request).id)
    profile = Profile.objects.get(user=user.id)
    return render_to_response('PersonalAccountExtension.html', {'user': user, 'profile': profile})


def personal_tests(request):
    user = User.objects.get(id=auth.get_user(request).id)
    profile = Profile.objects.get(user=user.id)
    finished_tests = profile.get_integer_finished_tests()
    return render_to_response('PersonalTests.html', {'user': user,
                                                     'tests': Test.objects.all().order_by('test_lesson_number'),
                                                     'finished_tests': finished_tests})


def change_profile_data(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            args["errors"] = "Ваши пароли должны совпадать!"
            return render_to_response('ChangeData.html', args)
        else:
            current_user = auth.get_user(request)
            current_user.set_password(password1)
            current_user.__setattr__("first_name", name)
            current_user.__setattr__("last_name", surname)
            current_user.save()
            auth.login(request, current_user)
            return redirect("/account/")
    else:
        return render_to_response('ChangeData.html', args)
