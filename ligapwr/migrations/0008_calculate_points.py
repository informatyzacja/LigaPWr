

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

def calculate_points(apps, schema_editor):
    from ..models import calculate_all_points
    calculate_all_points()

class Migration(migrations.Migration):

    dependencies = [
        ('ligapwr', '0007_add_dummy_data'),
    ]

    operations = [
        migrations.RunPython(
            calculate_points,
            reverse_code=migrations.RunPython.noop,
        )
    ]
