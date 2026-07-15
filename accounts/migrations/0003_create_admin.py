from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_admin(apps, schema_editor):
    User = apps.get_model("accounts", "User")

    User.objects.create(
        username="admin",
        email="admin@example.com",
        password=make_password("Admin@12345"),
        role="Admin",
        is_staff=True,
        is_superuser=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_otprecord"),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]