from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A Profile model that extends the User model in django auth
    """
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', "Don't specify"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Profile Pic', upload_to='accounts_img', default='accounts_img/logo.PNG')
    gender = models.CharField(
        max_length=30,
        choices=GENDER_CHOICE,
        default='Unknown'
    )
    address1 = models.CharField("Address line 1", max_length=1024, null=True)
    address2 = models.CharField("Address line 2", max_length=1024, null=True)
    city = models.CharField(max_length=1024, null=True)
    postcode = models.CharField( max_length=12, null=True)
    session_token = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'
