from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# local import of manager and other model
from .manager import CustomUserManager

#Function to upload file etc
def upload_image(instance, filename):
    return "image_folder/" + filename

def upload_file(instance, filename):
    return "file_folder/" + filename


class CustomUser(AbstractBaseUser, PermissionsMixin):
    SUBSCRIBE_TYPE = [
        ("FR", "Free tier"),
        ("LG", "Light tier"),
        ("PR", "Premium tier"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField(editable=True, null=True, blank=True)

    profile_img = models.ImageField(upload_to=upload_image, blank=True, null=True)
    subscribe_type = models.CharField(max_length=2, choices=SUBSCRIBE_TYPE, default="FR")

    # Exclude on serialization
    date_joined = models.DateTimeField(auto_now_add=True, editable=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
