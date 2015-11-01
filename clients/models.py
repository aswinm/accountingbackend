from django.db import models

class Client(models.Model):

    company_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=25)
    company_city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_projects = models.IntegerField(default=0,blank=True,null=True)
    total_income = models.FloatField(default=0,blank=True,null=True)

    def __unicode__(self):
        return self.company_name



# Create your models here.
