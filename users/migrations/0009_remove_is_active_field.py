from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_users_is_active_users_is_staff_users_last_login_and_more'),  # تغییر به مهاجرت قبلی خود
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
    ]