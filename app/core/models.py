from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email, password, and other fields."""
        # Use create_user to handle the common user creation
        user = self.create_user(email, password, **extra_fields)
        # Set superuser-specific flags
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True 

    def has_perm(self, perm, obj=None):
        return True  
