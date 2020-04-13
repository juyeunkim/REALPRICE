from django.utils import timezone
from django.db import models


class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20, null=True)
    area = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(max_length=10, null=True)
    longitude = models.FloatField(max_length=10, null=True)
    category = models.CharField(max_length=200, null=True)

    @property
    def category_list(self):
        return self.category.split("|") if self.category else []

class Faq(models.Model):
    faq_no = models.AutoField(primary_key=True)
    faq_category = models.CharField(max_length=100, null=False, default='other')
    faq_title = models.CharField(max_length=200, null=False)
    faq_content = models.TextField(null=True)
    faq_writer = models.CharField(max_length=100, null=False)
    faq_write_date = models.DateField()
    faq_answer = models.TextField(null=True)
    
    
class Qna(models.Model):
    qna_no = models.AutoField(primary_key=True)
    qna_group_no = models.IntegerField(null=False)
    qna_group_order = models.IntegerField(null=False)
    qna_depth = models.IntegerField(null=False)
    qna_title = models.CharField(max_length=200, null=False)
    qna_content = models.TextField(null=True)
    qna_writer = models.CharField(max_length=100, null=False)
    qna_write_date = models.DateField()

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    store = models.IntegerField(null=False)
    user = models.IntegerField(null=False)
    score = models.IntegerField(null=False)
    content = models.TextField(null=True)
    reg_time = models.DateField()

# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(blank=True, null=True,max_length=200)
    email = models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=4)
    born_year = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100) #nickname or realname
    address = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    tag = models.CharField(max_length = 500, blank=True)
    photo = models.ImageField(upload_to='uploads', blank=True)
