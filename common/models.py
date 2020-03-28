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
    

class Member(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    
    GENDERS = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    user = models.OneToOneField(
        User, related_name="user_member", on_delete=models.CASCADE,
        blank=True, null=True
    )
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20, unique=True, blank=True, null=True)
    gender = models.CharField(
        max_length=100, default=GENDER_MALE, choices=GENDERS,
        blank=True, null=True
    )
    step_id = models.IntegerField(blank=True, null=True, default=1)
    created_user = models.ForeignKey(
        User, blank=True, null=True,
        related_name='user_creation_member', on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
    


class Partner(models.Model):
    POSITION_LEFT = 'left'
    POSITION_RIGHT = 'right'

    POSITIONS = (
        (POSITION_LEFT, 'Left'),
        (POSITION_RIGHT, 'Right')
    )

    member_parent = models.ForeignKey(
        Member, related_name='member_as_parent', on_delete=models.CASCADE
    )

    member_child = models.ForeignKey(
        Member, related_name='member_as_child', on_delete=models.CASCADE,
         blank=True, null=True
    )

    position = models.CharField(
        max_length=100, default=POSITION_LEFT, choices=POSITIONS,
        blank=True, null=True
    )

    def __str__(self):
        return self.member_parent.name
    

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
