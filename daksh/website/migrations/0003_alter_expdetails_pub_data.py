# Generated by Django 4.0.2 on 2022-03-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_expdetails_pub_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expdetails',
            name='pub_data',
            field=models.DateTimeField(verbose_name='pub_date'),
        ),
    ]