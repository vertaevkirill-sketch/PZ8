import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
import django
django.setup()

from library.models import Author, Publisher, Book

print("=== ТЕСТ ЗАПРОСОВ ===")

# 1. Подсчет
print(f"1. Авторов в базе: {Author.objects.count()}")
print(f"2. Книг в базе: {Book.objects.count()}")

# 2. Простые выборки
print("\n3. Все авторы:")
for author in Author.objects.all():
    print(f"   - {author.first_name} {author.last_name}")

print("\n4. Все книги:")
for book in Book.objects.all():
    print(f"   - '{book.title}' - {book.price} руб.")

# 3. Фильтрация
print("\n5. Книги дороже 500 рублей:")
expensive = Book.objects.filter(price__gt=500)
for book in expensive:
    print(f"   - {book.title}: {book.price} руб.")

# 4. Связи
print("\n6. Книги Толстого:")
tolstoy_books = Book.objects.filter(author__last_name='Толстой')
for book in tolstoy_books:
    print(f"   - {book.title}")

# 5. Вычисляемые поля
if Book.objects.exists():
    book = Book.objects.first()
    print(f"\n7. Пример вычисляемых полей для '{book.title}':")
    print(f"   Цена: {book.price} руб.")
    print(f"   Цена с НДС: {book.price_with_vat} руб.")
    print(f"   Цена за страницу: {book.page_price_ratio:.4f} руб./стр.")

print("\n✅ Тесты завершены успешно!")
