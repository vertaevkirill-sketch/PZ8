import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
import django
django.setup()

from library.models import Author, Publisher, Book
from django.db.models import Count, Avg

print("=== ТЕСТОВЫЕ ЗАПРОСЫ ===")

# 1. Все авторы
print("1. Все авторы:")
for author in Author.objects.all():
    print(f"   - {author.first_name} {author.last_name} ({author.country})")

# 2. Все книги
print("\n2. Все книги:")
for book in Book.objects.all():
    print(f"   - {book.title} - {book.author} - {book.price} руб.")

# 3. Средняя цена книг
avg_price = Book.objects.aggregate(avg_price=Avg('price'))
print(f"\n3. Средняя цена книги: {avg_price['avg_price']:.2f} руб.")

# 4. Книги дороже 500 рублей
expensive = Book.objects.filter(price__gt=500)
print(f"\n4. Книг дороже 500 рублей: {expensive.count()}")

# 5. Создание новой записи
print("\n5. Создаем новую книгу...")
try:
    author = Author.objects.first()
    publisher = Publisher.objects.first()
    
    new_book = Book.objects.create(
        title='Тестовая книга',
        author=author,
        publisher=publisher,
        isbn='9781234567890',
        publication_date=date(2024, 1, 1),
        pages=100,
        price=500,
        rating=4.0,
        genre='FIC',
        format=1
    )
    print(f"   Создана: {new_book.title}")
    
    # Удаляем тестовую книгу
    new_book.delete()
    print("   Тестовая книга удалена")
except Exception as e:
    print(f"   Ошибка: {e}")

print("\n✅ Тесты завершены!")
