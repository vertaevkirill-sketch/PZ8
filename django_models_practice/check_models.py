import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
import django
django.setup()
print("✅ Models.py корректен, Django загружен успешно")
