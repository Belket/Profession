"""Profession URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Test import views as test_views
from LoginSys import views as auth_views
from Pages import views as pages_views
from PersonalAccount import views as account_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('home/', pages_views.home_page),  # Стартовая страница
    path('account/<current_login>/<current_id>', test_views.single_test),  # Конкретный тест
    path('account/reset_answers', account_views.reset_answers), # Очистить ответы пользователя
    path('auth/login/', auth_views.login),  # Страница авторизации
    path('auth/logout/', auth_views.logout),  # Выход из авторизации
    path('auth/registration/', auth_views.registration),  # Регистрация
    path('account/', account_views.personal_account),  # Вход в личный кабинет
    path('account/personal_tests/', account_views.personal_tests),
    path('account/changedata/', account_views.change_profile_data),  # Изменение данных профиля
    path('contact/',pages_views.contact_us),  # Контактная форма
    path('results/<current_login>/<current_test_id>', test_views.test_results),
    path('final_results/<current_login>/<current_test_id>', test_views.final_result),
    path('activate_user/<current_login>/<activation_salt>', account_views.activate_user),
    path('', pages_views.home_page),  # Только адрес сервера - на стартовую страницу
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
