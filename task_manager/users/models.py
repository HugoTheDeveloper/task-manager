from django.contrib.auth import models


# Create your models here.


class CustomUser(models.User):
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']


    def __str__(self):
        return self.get_full_name()

