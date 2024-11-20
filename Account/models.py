from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)  # Bio sahəsi
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Giriş üçün email istifadə olunur
    REQUIRED_FIELDS = ['full_name']  # Email-dən başqa tələb olunan sahələr

    def get_username(self):
        return self.username
