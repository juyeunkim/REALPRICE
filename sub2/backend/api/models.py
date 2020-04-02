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
    # faq_group_no = models.IntegerField(null=False)
    # faq_group_order = models.IntegerField(null=False)
    # faq_depth = models.IntegerField(null=False)
    faq_title = models.CharField(max_length=200, null=False)
    faq_content = models.TextField(null=True)
    faq_writer = models.CharField(max_length=100, null=False)
    faq_write_date = models.DateField()
    faq_count = models.IntegerField(null=False)
    
    
class Qna(models.Model):
    qna_no = models.AutoField(primary_key=True)
    # qna_group_no = models.IntegerField(null=False)
    # qna_group_order = models.IntegerField(null=False)
    # qna_depth = models.IntegerField(null=False)
    qna_title = models.CharField(max_length=200, null=False)
    qna_content = models.TextField(null=True)
    qna_writer = models.CharField(max_length=100, null=False)
    qna_write_date = models.DateField()
    qna_count = models.IntegerField(null=False)
