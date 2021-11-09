from django.db import models

# Create your models here.
class AI_summery(models.Model):
    total_calls= models.CharField(max_length=500,editable=True,null=True)
    Successful_calls= models.CharField(max_length=500,editable=True,null=True)
    Response_time= models.CharField(max_length=500,editable=True,null=True)
    Timestamp= models.CharField(max_length=500,editable=True,null=True)


class total_hits(models.Model):
    idd = models.IntegerField(primary_key = True)
    number_calls= models.CharField(max_length=500,editable=True,null=True)
    Successful_calls= models.CharField(max_length=500,editable=True,null=True)
def __str__(self):
    return self.total_calls