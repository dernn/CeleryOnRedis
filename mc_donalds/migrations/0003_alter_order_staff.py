# Generated by Django 4.0.5 on 2024-03-09 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mc_donalds', '0002_remove_productorder_amount_productorder__amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='mc_donalds.staff'),
        ),
    ]