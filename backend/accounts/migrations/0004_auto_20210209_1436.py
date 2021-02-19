# Generated by Django 3.1.1 on 2021-02-09 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210205_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccountmodel',
            name='author',
        ),
        migrations.RemoveField(
            model_name='useraccountmodel',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='useraccountmodel',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='useraccountmodel',
            name='shipping_address',
        ),
        migrations.DeleteModel(
            name='AddressModel',
        ),
        migrations.DeleteModel(
            name='CartModel',
        ),
        migrations.DeleteModel(
            name='UserAccountModel',
        ),
    ]