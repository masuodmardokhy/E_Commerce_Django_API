from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


 # To create a default admin user
User = get_user_model()
class Command(BaseCommand):
    help = 'Create admin user '

    def handle(self, *args, **options):
        admin_email = 'admin@example.com'
        admin_password = 'adminpassword'

        try:
            admin_user = User.objects.get(email=admin_email)
        except User.DoesNotExist:
            admin_user = User.objects.create_superuser(
                email=admin_email,
                user_name='admin',
                first_name='Admin',
                last_name='User',
                phone='1234567890',
                password=admin_password
            )
            self.stdout.write(self.style.SUCCESS('Admin user created successfully.'))
