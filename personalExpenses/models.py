from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userExpense(models.Model):
    uid = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
    January = models.JSONField(null=True)
    February = models.JSONField(null=True)
    March = models.JSONField(null=True)
    April = models.JSONField(null=True)
    May = models.JSONField(null=True)
    June = models.JSONField(null=True)
    July = models.JSONField(null=True)
    August = models.JSONField(null=True)
    September = models.JSONField(null=True)
    October = models.JSONField(null=True)
    November = models.JSONField(null=True)
    December = models.JSONField(null=True)
    
    def __str__(self):
        return self.uid