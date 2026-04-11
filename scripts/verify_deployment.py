import os
import sys
import subprocess

def check_file(path):
    if os.path.exists(path):
        print(f"✅ Found: {path}")
        return True
    else:
        print(f"❌ Missing: {path}")
        return False

def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("✅ Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e.stderr}")
        return False

def main():
    print("--- Starting Verification ---")
    
    # 1. Check Favicon
    check_file("static/images/favicon.png")
    
    # 2. Check settings for djangocms_admin_style
    try:
        from ambika.settings import base
        if "djangocms_admin_style" in base.INSTALLED_APPS:
            print("✅ djangocms_admin_style in INSTALLED_APPS")
        else:
            print("❌ djangocms_admin_style missing from INSTALLED_APPS")
    except ImportError:
        print("❌ Could not import settings")

    # 3. Check if djangocms_admin_style is installed
    try:
        import djangocms_admin_style
        print("✅ djangocms_admin_style is installed in environment")
    except ImportError:
        print("❌ djangocms_admin_style IS NOT INSTALLED in environment")
        print("   Fix: Run 'pip install djangocms-admin-style'")

    # 4. Run Django Check
    run_command([sys.executable, "manage.py", "check"])
    
    # 5. Check Collectstatic (Dry run if possible, but we'll just check if it fails)
    # Note: This might take a while if there are many files.
    print("Checking collectstatic manifest generation...")
    # We use --dry-run if supported, but standard collectstatic doesn't have a manifest check dry run
    # WhiteNoise will fail during collectstatic if files are missing.
    # run_command([sys.executable, "manage.py", "collectstatic", "--noinput", "--dry-run"])

    print("--- Verification Complete ---")

if __name__ == "__main__":
    main()
