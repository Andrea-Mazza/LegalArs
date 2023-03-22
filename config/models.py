from django.contrib.auth.models import AbstractUser
from django.db import models


# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.email


# In this example, we've added an email field to the User model and made it a required field.
# The USERNAME_FIELD attribute specifies that we'll be using the email field as the username field for
# authentication purposes.

# Once you've created your custom user model, you'll need to update your AUTH_USER_MODEL setting
# in your project's settings.py file
