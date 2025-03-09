from django.db import models



class Class(models.Model):
    course = models.CharField(max_length=9)
    activity = models.CharField(max_length=30)
    term = models.IntegerField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    days = models.CharField(max_length=50)

