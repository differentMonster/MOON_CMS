# Generated by Django 3.1.1 on 2021-02-05 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210204_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccountModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
        migrations.RemoveField(
            model_name='user',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='useraccountmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
        migrations.AddField(
            model_name='useraccountmodel',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='accounts.addressmodel'),
        ),
        migrations.AddField(
            model_name='useraccountmodel',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.cartmodel'),
        ),
        migrations.AddField(
            model_name='useraccountmodel',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='accounts.addressmodel'),
        ),
    ]