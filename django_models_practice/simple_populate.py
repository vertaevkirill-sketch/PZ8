import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
import django
django.setup()

from library.models import Author, Publisher, Book
from datetime import date

print("Начинаем заполнение базы данных...")

# Создаем авторов
authors = [
    Author.objects.create(
        first_name="Лев",
        last_name="Толстой",
        country="Россия",
        birth_date=date(1828, 9, 9)
    ),
    Author.objects.create(
        first_name="Фёдор",
        last_name="Достоевский",
        country="Россия",
        birth_date=date(1821, 11, 11)
    ),
    Author.objects.create(
        first_name="Александр",
        last_name="Пушкин",
        country="Россия",
        birth_date=date(1799, 6, 6)
    ),
]

print(f"✅ Создано авторов: {len(authors)}")

# Создаем издательства
publishers = [
    Publisher.objects.create(
        name="Эксмо",
        publisher_type="COM",
        founded_year=1991
    ),
    Publisher.objects.create(
        name="АСТ",
        publisher_type="COM",
        founded_year=1990
    ),
]

print(f"✅ Создано издательств: {len(publishers)}")

# Создаем книги
books = [
    Book.objects.create(
        title="Война и мир",
        author=authors[0],
        publisher=publishers[0],
        isbn="9785171203604",
        publication_date=date(2020, 1, 15),
        pages=1274,
        price=1200.00,
        rating=4.8,
        genre="FIC",
        format=2
    ),
    Book.objects.create(
        title="Преступление и наказание",
        author=authors[1],
        publisher=publishers[1],
        isbn="9785170878858",
        publication_date=date(2019, 5, 20),
        pages=608,
        price=450.00,
        rating=4.7,
        genre="FIC",
        format=1
    ),
    Book.objects.create(
        title="Евгений Онегин",
        author=authors[2],
        publisher=publishers[0],
        isbn="9785170987650",
        publication_date=date(2018, 7, 5),
        pages=320,
        price=300.00,
        rating=4.6,
        genre="FIC",
        format=1
    ),
]

print(f"✅ Создано книг: {len(books)}")
print("\n=== СТАТИСТИКА ===")
print(f"Всего авторов: {Author.objects.count()}")
print(f"Всего издательств: {Publisher.objects.count()}")
print(f"Всего книг: {Book.objects.count()}")
print("\n✅ База данных успешно заполнена!")
