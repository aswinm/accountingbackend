from django.db import models
from django.db.models import Sum
from clients.models import Client

import datetime

class Project(models.Model):

    def __unicode__(self):
        return str(self.id)

    def set_duration_string(self):
        seconds = self.total_duration_num
        minutes = seconds / 60
        hours = minutes / 60
        minutes = minutes % 60
        self.total_duration = str(hours) + " hours " + str(minutes) + " minutes "
        self.save()

    def create(self, *args, **kwargs):
        super(Project, self).create(*args,**kwargs)
        self.client.total_income += self.total_income
        self.client.save()

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        projects = self.client.projects.all()
        total_income = 0
        for project in projects:
            total_income += project.total_cost

        self.client.total_income = total_income
        self.client.save()

    def delete(self):
        client = self.client
        client.no_of_projects -= 1
        client.total_income -= self.total_cost
        client.save()
        super(Project, self).delete()

    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client,related_name='projects')
    total_cost = models.FloatField()
    total_duration_num = models.IntegerField(default=0)
    total_duration = models.CharField(max_length=255,default="")

class TimeDuration(models.Model):

    def __unicode__(self):
        return str(self.id)

    def delete(self):
        #from_time = datetime.datetime.strptime(self.from_time, "%Y-%m-%d %H:%M:%S")
        #to_time = datetime.datetime.strptime(self.to_time, "%Y-%m-%d %H:%M:%S")
        duration = int((self.to_time - self.from_time).total_seconds())
        self.project.total_duration_num -= duration
        self.project.save()
        self.project.set_duration_string()
        super(TimeDuration, self).delete()

    from_time = models.CharField(max_length=255)
    to_time = models.CharField(max_length=255)
    duration = models.CharField(max_length=255,blank=True,null=True)
    project = models.ForeignKey(Project,related_name="time_durations")

# Create your models here.
