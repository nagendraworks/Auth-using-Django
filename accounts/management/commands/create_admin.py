from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = "Create admin user"

    def handle(self, *args, **kwargs):

        user = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password="Admin@12345",
            role="Admin"
        )

        user.is_staff = True
        user.is_superuser = True
        user.save()

        self.stdout.write(
            self.style.SUCCESS("Admin created successfully")
        )
