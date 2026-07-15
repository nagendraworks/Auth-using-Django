from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_admin(apps, schema_editor):
    CustomUser = apps.get_model("accounts", "CustomUser")

    if not CustomUser.objects.filter(username="admin").exists():
        CustomUser.objects.create(
            username="admin",
            email="admin@example.com",
            password=make_password("Admin@12345"),
            role="ADMIN",
            is_staff=True,
            is_superuser=True,
        )


def remove_admin(apps, schema_editor):
    CustomUser = apps.get_model("accounts", "CustomUser")
    CustomUser.objects.filter(username="admin").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_otprecord"),
    ]

    operations = [
        migrations.RunPython(create_admin, remove_admin),
    ]