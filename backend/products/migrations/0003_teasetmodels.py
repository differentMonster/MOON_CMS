# Generated by Django 3.0.7 on 2020-07-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200716_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeasetModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, default='default.png', max_length=200, upload_to='')),
                ('photo2', models.ImageField(blank=True, default='default2.png', max_length=200, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
