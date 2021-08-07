from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    added_date = models.DateField()
    todo = models.CharField(max_length=200)


# here we are adding additional information class for default User class

class UserProfileInfo(models.Model):

    # default User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE,)

    # adding additional fields to default User Model
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        return self.user.username