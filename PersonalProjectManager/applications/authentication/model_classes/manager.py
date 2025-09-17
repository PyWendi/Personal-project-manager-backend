from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    """
    Create a custom user manager for custom user model
    """
    def create_user(self, email:str , password:str=None, **extra_fields):
        if not email:
            raise ValueError("The email must not be empty")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        # user.password = make_password(password)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email:str, password:str=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)