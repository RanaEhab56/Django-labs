from django.db import models
from django.utils.translation import gettext_lazy as _

class Actor(models.Model):
    NATIONALITIES = (
        ('eg','Egyptian'),
        ('ksa','Saudi Arabian'),
        ('kwait','Kuwait Citizen'),
    )
    GENDER = (
        ('m','male'),
        ('f','female'),
    )
    name=models.fields.CharField(verbose_name=_('Actor'),max_length=50)
    gender=models.fields.CharField(choices=GENDER,max_length=1,default='m')
    age=models.fields.PositiveIntegerField()
    nationality=models.fields.CharField(choices=NATIONALITIES,max_length=6)

    def __str__(self):
        return self.name

