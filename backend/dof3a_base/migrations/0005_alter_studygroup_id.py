# Generated by Django 5.2.4 on 2025-07-23 18:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dof3a_base", "0004_alter_student_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studygroup",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
