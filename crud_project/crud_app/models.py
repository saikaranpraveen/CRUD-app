from django.db import models

class profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    contact = models.CharField(max_length=15)
    class Meta:
        db_table = "profile"

  