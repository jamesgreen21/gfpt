# Generated by Django 3.0.5 on 2020-04-13 17:53

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200412_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='accounts_img/logo.PNG', upload_to='accounts_img', verbose_name='Profile Pic'),
        ),
    ]
