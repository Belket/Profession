from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User
from datetime import datetime, timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.CharField(max_length=8, default="")
    city_of_residence = models.CharField(max_length=30, default="")
    country_of_residence = models.CharField(max_length=30, default="")
    available_tests = models.CharField(max_length=1000, validators=[validate_comma_separated_integer_list])
    finished_tests = models.CharField(max_length=1000, validators=[validate_comma_separated_integer_list])
    activation_salt = models.CharField(max_length=30, default="none")

    def __str__(self):
        return self.user.username

    def get_integer_finished_tests(self):
        integers_finished_tests = []
        finished_tests = self.finished_tests
        string_finished_tests = finished_tests.split(",")
        if len(string_finished_tests) == 1 and '' in string_finished_tests:
            return integers_finished_tests
        else:
            integers_finished_tests = [int(id_elem) for id_elem in string_finished_tests]
            return integers_finished_tests

    def reset_test(self):
        self.finished_tests = ""
        self.save()

    def add_finished_test(self, new_finished_test):
        if self.finished_tests == "":
            self.finished_tests = self.finished_tests + str(new_finished_test)
        else:
            self.finished_tests = self.finished_tests + "," + str(new_finished_test)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.profile = Profile.objects.create(user=instance)
    instance.profile.save()

