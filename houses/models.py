from django.db import models

# Create your models here.

class House(models.Model):

    """ Model Definition for Houses """

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)
    
    """ models.Model 클래스로 부터 상속받은 houses의 object name을 self,name으로 오버라이딩 """
    def __str__(self):
        return self.name


    