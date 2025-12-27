import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
import django
django.setup()

from library.models import Author, Publisher, Book, Review
from django.db.models import Count, Avg, Sum, Max, Min

print("=== ДЕМОНСТРАЦИЯ РАБОТЫ С МОДЕЛЯМИ DJANGO ===\n")

# 1. Базовые запросы
print("1. Все авторы из России:")
russian_authors = Author.objects.filter(country='Россия')
for author in russian_authors:
    print(f"   - {author.full_name}")

# 2. Сложные запросы с агрегацией
print("\n2. Статистика по книгам:")
stats = Book.objects.aggregate(
    total_books=Count('id'),
    avg_price=Avg('price'),
    max_price=Max('price'),
    min_price=Min('price'),
    total_pages=Sum('pages')
)
for key, value in stats.items():
    print(f"   {key}: {value}")

# 3. Запросы со связями
print("\n3. Книги издательства 'Эксмо':")
eksmo_books = Book.objects.filter(publisher__name='Эксмо')
for book in eksmo_books:
    print(f"   - {book.title} ({book.author})")

# 4. Аннотации
print("\n4. Авторы с количеством книг:")
authors_with_counts = Author.objects.annotate(book_count=Count('books')).order_by('-book_count')
for author in authors_with_counts[:5]:
    print(f"   - {author.full_name}: {author.book_count} книг")

# 5. Использование вычисляемых полей
print("\n5. Вычисляемые поля (пример для первой книги):")
book = Book.objects.first()
if book:
    print(f"   Книга: {book.title}")
    print(f"   Цена: {book.price} руб.")
    print(f"   Цена с НДС: {book.price_with_vat} руб.")
    print(f"   Цена за страницу: {book.page_price_ratio:.4f} руб./стр.")
    print(f"   Новая книга: {'Да' if book.is_new else 'Нет'}")

# 6. Создание новой записи
print("\n6. Создание нового автора:")
try:
    new_author = Author.objects.create(
        first_name="Иван",
        last_name="Тургенев",
        country="Россия",
        birth_date="1818-11-09"
    )
    print(f"   Создан автор: {new_author.full_name}")
    
    # Создаем книгу для нового автора
    new_book = Book.objects.create(
        title="Отцы и дети",
        author=new_author,
        isbn="9785171234567",
        publication_date="2023-05-15",
        pages=320,
        price=400,
        rating=4.5,
        genre='FIC',
        format=1
    )
    print(f"   Создана книга: '{new_book.title}'")
    
except Exception as e:
    print(f"   Ошибка: {e}")

# 7. Обновление записи
print("\n7. Обновление цены книги:")
book_to_update = Book.objects.filter(title__contains='Гарри Поттер').first()
if book_to_update:
    old_price = book_to_update.price
    book_to_update.price = 850
    book_to_update.save()
    print(f"   Обновлена цена для '{book_to_update.title}': {old_price} -> {book_to_update.price} руб.")

# 8. Удаление записи (осторожно!)
print("\n8. Удаление тестового автора (если существует):")
test_authors = Author.objects.filter(first_name="Иван", last_name="Тургенев")
if test_authors.exists():
    deleted_count, _ = test_authors.delete()
    print(f"   Удалено записей: {deleted_count}")

print("\n=== ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА ===")
