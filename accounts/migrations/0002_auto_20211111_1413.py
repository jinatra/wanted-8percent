# Generated by Django 3.2.9 on 2021-11-11 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', unique=True),
        ),
    ]
