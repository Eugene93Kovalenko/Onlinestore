from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from users_app.models import CustomUser


# class EmailAuthBackend(ModelBackend):
#     """
#     Custom authentication backend.
#
#     Allows users to log in using their email address.
#     """
#
#     def authenticate(self, request, username=None, password=None):
#         """
#         Overrides the authenticate method to allow users to log in using their email address.
#         """
#         try:
#             user = CustomUser.objects.get(email=username)
#             if user.check_password(password):
#                 return user
#             return None
#         except CustomUser.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         """
#         Overrides the get_user method to allow users to log in using their email address.
#         """
#         try:
#             return CustomUser.objects.get(pk=user_id)
#         except CustomUser.DoesNotExist:
#             return None


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user = get_user_model()
        try:
            user = user.objects.get(email=email)
        except user.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        user = get_user_model()
        try:
            return user.objects.get(pk=user_id)
        except user.DoesNotExist:
            return None
