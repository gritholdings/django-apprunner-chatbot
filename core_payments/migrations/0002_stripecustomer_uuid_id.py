# Generated by Django 5.1.4 on 2024-12-31 15:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripecustomer',
            name='uuid_id',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]