# Generated by Django 3.0.4 on 2020-03-27 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='created_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_creation_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
