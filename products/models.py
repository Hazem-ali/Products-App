from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)  # create a model

        user.set_password(password)  # Hashes the password
        user.save(using=self._db)  # Important to save to db

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)

    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name for user"""
        return f"{self.name}" 

# Create your models here.

# class Order(models.Model):

#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     pass

class Product(models.Model):
    name = models.CharField( max_length=255)
    price = models.FloatField()
    inventory = models.IntegerField()

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Order(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    product = models.ManyToManyField(Product)

    quantity = models.IntegerField()
    created_on = models.DateTimeField(  auto_now_add=True, null=True)

