from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
from django.db import models

# Create your models here.
class Person(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

        

class Property(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    address = models.TextField(max_length=250,blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)

    
class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units',blank=True, null=True)
    type_choices = [
        ('1BHK', '1 Bedroom'),
        ('2BHK', '2 Bedrooms'),
        ('3BHK','3 Bedrooms'),
        ('4BHK','4 Bedrooms')
    ]
    unit_type = models.CharField(max_length=10, choices=type_choices,blank=True, null=True)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)


class TenantProfile(models.Model):
    name = models.CharField(_("name"), max_length=50, blank=True, null=True)
    address = models.TextField(max_length=250, blank=True, null=True)
    DOCUMENT_TYPES = [
        ('passport', 'Passport'),
        ('license', 'Driver License'),
        ('id_card', 'ID Card'),
    ]
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES, blank=True, null=True)
    document_proof = models.FileField(upload_to='document_proofs/', blank=True, null=True)


class Tenant(models.Model):
    tenant_profile = models.OneToOneField(TenantProfile, on_delete=models.CASCADE, related_name='tenant', blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='tenants', blank=True, null=True)
    agreement_end_date = models.DateField(blank=True, null=True)
    monthly_rent_date = models.IntegerField(blank=True, null=True)

    
