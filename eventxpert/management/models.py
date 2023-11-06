from django.db import models

# Create your models here.
class TestModel(models.Model):
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
