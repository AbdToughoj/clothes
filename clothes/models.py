from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.
class Clothe(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField()
    purchaser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('clothe_list')
    