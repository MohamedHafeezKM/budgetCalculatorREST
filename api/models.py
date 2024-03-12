from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    type_choice=(('expense','expense'),('income','income'))
    type=models.CharField(max_length=50,choices=type_choice)
    category_choice=(('miscellaneous','miscellaneous'),
                     ('food','food'),
                     ('shopping','shopping'),
                     ('rent','rent'),
                     ('fuel','fuel'),
                     )
    
    category=models.CharField(max_length=60,choices=category_choice)
    amount=models.IntegerField()
    

