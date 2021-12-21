from django.db import models
from django.contrib.auth.models import User

class Turn(models.Model):
    customer_name=models.CharField(max_length = 50)
    Name_Barber_Choices = (
        ('1','Amin'),
        ('2','Mehrdad'),
        ('3','Navid'),
        ('4','Nima'),
    )
    name_barber = models.CharField(max_length=1, choices=Name_Barber_Choices)
    slug= models.SlugField()
    registration_time=models.DateTimeField(auto_now_add = True)
    date=models.DateTimeField()
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)



    def __str__(self):
        return self.customer_name
