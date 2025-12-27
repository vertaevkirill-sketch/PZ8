import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
import django
django.setup()

from library.models import Author, Publisher, Book, Review
from django.db import transaction
from datetime import date

print("Начинаем заполнение базы данных тестовыми данными...")

with transaction.atomic():
    # Создаем авторов
    authors_data = [
        {'first_name': 'Лев', 'last_name': 'Толстой', 'country': 'Россия', 'birth_date': date(1828, 9, 9)},
        {'first_name': 'Фёдор', 'last_name': 'Достоевский', 'country': 'Россия', 'birth_date': date(1821, 11, 11)},
        {'first_name': 'Антон', 'last_name': 'Чехов', 'country': 'Россия', 'birth_date': date(1860, 1, 29)},
        {'first_name': 'Александр', 'last_name': 'Пушкин', 'country': 'Россия', 'birth_date': date(1799, 6, 6)},
    ]
    
    authors = []
    for author_data in authors_data:
        author, created = Author.objects.get_or_create(
            first_name=author_data['first_name'],
            last_name=author_data['last_name'],
            defaults=author_data
        )
        authors.append(author)
        if created:
            print(f"  Создан автор: {author}")
    
    # Создаем издательства
    publishers_data = [
        {'name': 'Эксмо', 'publisher_type': 'COM', 'founded_year': 1991},
        {'name': 'АСТ', 'publisher_type': 'COM', 'founded_year': 1990},
        {'name': 'Просвещение', 'publisher_type': 'STA', 'founded_year': 1930},
    ]
    
    publishers = []
    for pub_data in publishers_data:
        publisher, created = Publisher.objects.get_or_create(
            name=pub_data['name'],
            defaults=pub_data
        )
        publishers.append(publisher)
        if created:
            print(f"  Создано издательство: {publisher}")
    
    # Создаем книги
    books_data = [
        {'title': 'Война и мир', 'author': authors[0], 'isbn': '9785171203604', 
         'publication_date': date(2020, 1, 15), 'pages': 1274, 'price': 1200, 
         'rating': 4.8, 'genre': 'FIC', 'format': 2, 'publisher': publishers[0]},
        
        {'title': 'Преступление и наказание', 'author': authors[1], 'isbn': '9785170878858', 
         'publication_date': date(2019, 5, 20), 'pages': 608, 'price': 450, 
         'rating': 4.7, 'genre': 'FIC', 'format': 1, 'publisher': publishers[1]},
        
        {'title': 'Евгений Онегин', 'author': authors[3], 'isbn': '9785170987650', 
         'publication_date': date(2018, 7, 5), 'pages': 320, 'price': 300, 
         'rating': 4.6, 'genre': 'FIC', 'format': 1, 'publisher': publishers[2]},
    ]
    
    books = []
    for book_data in books_data:
        book, created = Book.objects.get_or_create(
            isbn=book_data['isbn'],
            defaults=book_data
        )
        books.append(book)
        if created:
            print(f"  Создана книга: {book.title}")
    
    print("\n✅ База данных успешно заполнена!")
    print(f"\n=== СТАТИСТИКА ===")
    print(f"Авторов: {Author.objects.count()}")
    print(f"Издательств: {Publisher.objects.count()}")
    print(f"Книг: {Book.objects.count()}")
