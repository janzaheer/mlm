from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    
    GENDERS = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    mobile = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(
        max_length=100, default=GENDER_MALE, choices=GENDERS,
        blank=True, null=True
    )

    def __str__(self):
        return self.user.username
    

class Partner(models.Model):
    POSITION_LEFT = 'left'
    POSITION_RIGHT = 'right'

    POSITIONS = (
        (POSITION_LEFT, 'Left'),
        (POSITION_RIGHT, 'Right')
    )

    user = models.ForeignKey(
        User, related_name='user_partner', on_delete=models.CASCADE
    )
    partner_user = models.ForeignKey(
        User, related_name='user_as_partner', on_delete=models.SET_NULL,
        blank=True, null=True
    )
    position = models.CharField(
        max_length=100, default=POSITION_LEFT, choices=POSITIONS,
        blank=True, null=True
    )
    step_id = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return self.user.username
    

# Signal Functions
def create_profile(sender, instance, created, **kwargs):
    """
    The functions used to check if user profile is not created
    and created the user profile without saving role and hospital
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created and not UserProfile.objects.filter(user=instance):
        return UserProfile.objects.create(
            user=instance
        )

# Signals
post_save.connect(create_profile, sender=User)
