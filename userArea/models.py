from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
# Create your models here.


def get_current_user():
    return get_user_model().objects.get_current()


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None, **extra_fields):
        if not email:
            raise ValueError('Il campo email deve essere compilato.')
        if not name:
            raise ValueError('Il campo nome deve essere compilato.')
        if not surname:
            raise ValueError('Il campo cognome deve essere compilato.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          surname=surname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password=password, **extra_fields)

    def create_custom_user(self, email, name, surname, password=None, **extra_fields):
        if not email:
            raise ValueError('Il campo email deve essere compilato.')
        if not name:
            raise ValueError('Il campo nome deve essere compilato.')
        if not surname:
            raise ValueError('Il campo cognome deve essere compilato.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          surname=surname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, default='')
    surname = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=30, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_viewed_servizi_attivi = models.DateTimeField(null=True, blank=True)
    has_subscription = models.BooleanField(default='False')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_short_name(self):
        return self.name

    class Meta:
        app_label = 'userArea'


# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return self.email

#     def get_short_name(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     class Meta:
#         app_label = 'userArea'


# In this example, we've added an email field to the User model and made it a required field.
# The USERNAME_FIELD attribute specifies that we'll be using the email field as the username field for
# authentication purposes.

# Once you've created your custom user model, you'll need to update your AUTH_USER_MODEL setting
# in your project's settings.py file
