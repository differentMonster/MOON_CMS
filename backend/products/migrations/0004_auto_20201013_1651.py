# Generated by Django 3.1.1 on 2020-10-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_teasetmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheongsammodels',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
