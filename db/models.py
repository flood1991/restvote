from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin
                                        )


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Create and return a `User` with an email, phone number, username and password.
        """
        if not email:
            raise ValueError("Users must have an email.")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if not password:
            raise ValueError("Superusers must have a password.")
        if not email:
            raise ValueError("Superusers must have an email.")

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Restaurant(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Employee(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(db_index=True, max_length=30)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Menu(models.Model):
    file = models.FileField(upload_to='media/')
    created_at = models.DateField(auto_now_add=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)

    def total_votes(self):
        return self.votes.count()

    def __str__(self):
        return self.restaurant.title


class Vote(models.Model):
    employee = models.ForeignKey(
        Employee, related_name='votes', on_delete=models.CASCADE)
    menu = models.ForeignKey(
        Menu, related_name='votes', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee}'
