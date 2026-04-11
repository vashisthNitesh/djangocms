import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ambika.settings.base')
django.setup()

from django.contrib.sites.models import Site
from djangocms_versioning.models import Version
from django.contrib.auth import get_user_model

def main():
    print("--- Making Site Live ---")

    # 1. Update Site Domain
    try:
        site = Site.objects.get(id=1)
        site.domain = 'niteshvashisth.pythonanywhere.com'
        site.name = 'Shri Ambika Sanskrit Mahavidyalaya'
        site.save()
        print(f"✅ Updated Site {site.id}: {site.domain} ({site.name})")
    except Exception as e:
        print(f"❌ Failed to update Site: {e}")

    # 2. Find any Admin User
    User = get_user_model()
    admin_user = User.objects.filter(is_superuser=True).first()
    if not admin_user:
        print("❌ No admin user found to publish version.")
        return

    # 3. Publish Version 8 (or the latest draft)
    try:
        # We target Version 8 as specified in the populate script
        v = Version.objects.get(number=8)
        if v.state != 'published':
            v.publish(admin_user)
            print(f"✅ Successfully published Version {v.number} of '{v.content.page}'")
        else:
            print(f"ℹ️ Version {v.number} is already published.")
    except Version.DoesNotExist:
        print("ℹ️ Version 8 not found. Searching for latest Draft...")
        v = Version.objects.filter(state='draft').order_by('-number').first()
        if v:
            v.publish(admin_user)
            print(f"✅ Successfully published latest draft version {v.number} of '{v.content.page}'")
        else:
            print("❌ No draft versions found to publish.")
    except Exception as e:
        print(f"❌ Failed to publish version: {e}")

    print("--- Done ---")
    print("\n👉 IMPORTANT: Please run 'python manage.py collectstatic --noinput --clear' now to update your icons!")
    print("👉 Then restart your PythonAnywhere web app.")

if __name__ == "__main__":
    main()
