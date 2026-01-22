from django.contrib.auth import get_user_model
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

User = get_user_model()
email = '008snk@gmail.com'
password = 'Manjil@1982'

try:
    if not User.objects.filter(email=email).exists():
        username = email.split('@')[0]
        user = User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser created successfully: {email}")
    else:
        print(f"User with email {email} already exists.")
except Exception as e:
    print(f"Error creating user: {e}")
