# Generated by Django 2.2.28 on 2022-06-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20220628_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsignup',
            old_name='dob',
            new_name='DATE_OF_BIRTH',
        ),
        migrations.RenameField(
            model_name='studentsignup',
            old_name='FirstName',
            new_name='FIRSTNAME',
        ),
        migrations.RenameField(
            model_name='studentsignup',
            old_name='LastName',
            new_name='LASTNAME',
        ),
        migrations.RenameField(
            model_name='studentsignup',
            old_name='password',
            new_name='PASSWORD',
        ),
        migrations.RemoveField(
            model_name='studentsignup',
            name='mail',
        ),
        migrations.AddField(
            model_name='studentsignup',
            name='EMAIL',
            field=models.EmailField(default='citizen0@utopia.com', max_length=254),
        ),
        migrations.AddField(
            model_name='studentsignup',
            name='GENDER',
            field=models.BooleanField(default=None),
        ),
    ]