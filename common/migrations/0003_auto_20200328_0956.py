# Generated by Django 3.0.4 on 2020-03-28 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20200327_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='step_id',
        ),
        migrations.AlterField(
            model_name='partner',
            name='member_child',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_as_child', to='common.Member'),
        ),
    ]
