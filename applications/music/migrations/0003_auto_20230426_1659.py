# Generated by Django 2.2.6 on 2023-04-26 16:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='parent_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
    ]
