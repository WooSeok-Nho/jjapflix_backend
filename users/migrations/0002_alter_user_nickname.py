<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-11-02 11:31
=======
# Generated by Django 4.1.3 on 2022-11-02 12:56
>>>>>>> 7f644ac28c4365267152dad5c1ad7a0b7e3c86ab

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=50),
        ),
    ]
