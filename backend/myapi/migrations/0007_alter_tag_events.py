# Generated by Django 5.0.3 on 2024-04-18 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_alter_event_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='events',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='myapi.event'),
        ),
    ]
