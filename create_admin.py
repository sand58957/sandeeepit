from django.contrib.auth import get_user_model
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

User = get_user_model()
email = '008snk@gmail.com'
password = 'Manjil@1982'

try:
    username = email.split('@')[0]
    user, created = User.objects.get_or_create(email=email, defaults={'username': username})
    
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()
    
    if created:
        print(f"✅ Superuser created successfully: {email}")
    else:
        print(f"✅ Superuser updated successfully (password reset): {email}")
    
    print(f"🔑 You can now log in with:")
    print(f"   Email: {email}")
    print(f"   Username: {user.username}")
    print(f"   Password: {password}")

except Exception as e:
    print(f"❌ Error setting up admin user: {e}")
