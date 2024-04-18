from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapi.models import Event

def create_group_and_permissions(apps, schema_editor):
    # get the content type for the Event model
    event_content_type = ContentType.objects.get_for_model(Event)

    # create the 'event' permission
    event_permission = Permission.objects.create(
        codename='manage_event',
        name='Can manage event',
        content_type=event_content_type,
    )

    # create the 'organizer' group
    organizer_group = Group.objects.create(name='organizer')

    # add the permissions to the group
    organizer_group.permissions.add(event_permission)

class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_tag_events'),  # replace with the name of the previous migration
    ]

    operations = [
        migrations.RunPython(create_group_and_permissions),
    ]