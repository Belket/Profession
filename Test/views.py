from django.contrib import auth
from django.shortcuts import render_to_response, render, redirect, HttpResponse
from Test.models import Test, QuestionWithVariants, QuestionWithAnswer, UsersAnswers, Hint, Results
from Profile.models import Profile
from django.contrib.auth.models import User
from Test import results_analisers as analise
from django.template import RequestContext
from Pages.models import HelpFunctions
# Create your views here.


def all_tests(request):
    return render_to_response('PersonalAccountExtension.html', {'tests': Test.objects.all(),
                                                                'user': User.objects.get(username=auth.get_user(request).username)})


def single_test(request, current_login="MissLog",  current_id="1"):
    finished = 0
    help_func = HelpFunctions()
    current_user = User.objects.get(username=current_login)
    profile = Profile.objects.get(user=current_user.id)
    finished_tests = profile.get_integer_finished_tests()
    if int(current_id) in finished_tests:
        finished = 1
    current_test = Test.objects.get(id=current_id)
    questions_with_answer = list(current_test.questionwithanswer_set.values())
    questions_with_variants = list(current_test.questionwithvariants_set.values())
    questions_type = [questions_with_answer, questions_with_variants]

    if request.POST:
        for question_type in questions_type:
            for question in range(len(question_type)):
                current_question = question_type[question]
                question_id = current_question.get("id")
                question_is_radio = current_question.get("question_with_one_answer")
                if question_is_radio:
                    answer = request.POST.get(str(question_id))
                else:
                    answer = ",".join(request.POST.getlist(str(question_id)))
                answer_model = UsersAnswers(user=User.objects.get(id=current_user.id),
                                            test=Test.objects.get(id=current_id),
                                            question_id=question_id,
                                            question_text=current_question.get("question_text"),
                                            user_answer=answer)
                answer_model.save()

        return redirect("/results/" + str(current_login) + '/' + str(current_id))

    else:
        # *********** Вопросы с ответами ************
        for question in range(len(questions_with_answer)):  # проходимся по всем вопросам с ответами
            recognized_words = []  # список для слов, нуждающихся в уточнении
            hint_text = ""  # текст подсказки
            current_question = questions_with_answer[question]  # получаем текущий вопрос
            recognized_words += help_func.is_hint_need(current_question.get("question_text"))
            recognized_words = list(set(recognized_words))  # убираем повторные слова
            for word in recognized_words:  # проходимся по всем словам, нуждающимся в уточнении
                current_hint = Hint.objects.get(defined_word=word)
                hint_text += current_hint.defined_word + ": " + current_hint.hint + "***"  # формируем текст подсказки

            current_question.update({'hint': hint_text})  # дополняем словарь с параметрами вопроса подсказкой

        # *************  Вопросы с вариантами ответов ****************
        for question in range(len(questions_with_variants)):
            recognized_words = []
            hint_text = ""
            current_question = questions_with_variants[question]
            line_with_answers = current_question.get("question_variants")
            answers = [variant.strip() for variant in line_with_answers.split(';')]
            current_question.update({"question_variants": answers})
            recognized_words += help_func.is_hint_need(answers)
            recognized_words += help_func.is_hint_need(current_question.get("question_text"))
            recognized_words = list(set(recognized_words))
            print("RECOGNIZED WORDS IN VIEWS:", recognized_words)
            for word in recognized_words:
                current_hint = Hint.objects.get(defined_word=word)
                hint_text += current_hint.defined_word + ": " + current_hint.hint + "***"
            current_question.update({'hint': hint_text})
            print("************\n", current_question, "\n************")

        return render(request, 'SingleTestExtension.html', {'test': current_test,
                                                            'questions_with_answer': questions_with_answer,
                                                            'questions_with_variants': questions_with_variants,
                                                            'user': current_user,
                                                            'finished': finished})


def test_results(request, current_login="MissLog", current_test_id="1"):

    current_user = User.objects.get(username=current_login)
    current_test = Test.objects.get(id=current_test_id)
    current_user.profile.add_finished_test(current_test.id)
    current_user.save()

    functions_for_analise = {1: analise.analise_results_test_1,
                             2: analise.analise_results_test_2,
                             3: analise.analise_results_test_3,
                             4: analise.analise_results_test_4,
                             5: analise.analise_results_test_5,
                             6: analise.analise_results_test_6,
                             7: analise.analise_results_test_7,
                             8: analise.analise_results_test_8,
                             9: analise.analise_results_test_9,
                             10: analise.analise_results_test_10,
                             11: analise.analise_results_test_11,
                             12: analise.analise_results_test_12,
                             13: analise.analise_results_test_13,
                             14: analise.analise_results_test_14,
                             15: analise.analise_results_test_15,
                             16: analise.analise_results_test_16, }

    result = functions_for_analise.get(current_test.test_lesson_number)(current_user.id, current_test_id)

    if request.POST:
        results = request.POST.get('result')
        test_number = request.POST.get('test_number')
        tests_dict = {"1": "first_test_result", "2": "second_test_result", "3": "third_test_result",
                      "4": "fourth_test_result", "5": "fifth_test_result", "6": "six_test_result",
                      "7": "seventh_test_result", "8": "eighth_test_result", "9": "ninth_test_result",
                      "10": "tenth_test_result", "11": "eleventh_test_result", "12": "twelfth_test_result",
                      "13": "thirteenth_test_result", "14": "fourteenth_test_result", "15": "fifteenth_test_result"}

        result_model, created = Results.objects.get_or_create(user_id=auth.get_user(request), test_id=current_test)
        model_code = "result_model." + tests_dict.get(str(test_number)) + "=\"" + results + "\""
        exec(model_code)
        result_model.save()
        return render_to_response("TestResults.html", {"test": current_test, "user": current_user, "result": result,
                                                       "lesson_number": current_test.test_lesson_number})
    else:
        return render_to_response("TestResults.html", {"test": current_test, "user": current_user, "result": result,
                                                       "lesson_number": current_test.test_lesson_number})


def final_result(request, current_login="MissLog", current_test_id="1"):
    current_user = User.objects.get(username=current_login)
    current_test = Test.objects.get(id=current_test_id)
    appropriate_professions = final_result(current_user.id, current_test.id)
    return render_to_response("FinalResults.html", {"professions": appropriate_professions})
