# Generated by Django 5.0.3 on 2024-05-09 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myapi', '0004_organizer_managed_events_alter_customer_events_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customer_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='organizer_groups', to='auth.group'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customers', models.ManyToManyField(blank=True, related_name='customer_groups', to='myapi.customer')),
                ('organizers', models.ManyToManyField(blank=True, related_name='organizer_groups', to='myapi.organizer')),
            ],
        ),
    ]
