# Generated by Django 4.2.5 on 2023-10-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Park', '0004_alter_user_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='current_mileage',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=15),
            preserve_default=False,
        ),
    ]
