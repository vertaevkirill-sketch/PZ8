import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from library.models import Author, Publisher, Book, Review
from django.db import transaction

print("Начинаем заполнение базы данных тестовыми данными...")

with transaction.atomic():
    # Создаем авторов
    authors_data = [
        {'first_name': 'Лев', 'last_name': 'Толстой', 'country': 'Россия', 'birth_date': date(1828, 9, 9)},
        {'first_name': 'Фёдор', 'last_name': 'Достоевский', 'country': 'Россия', 'birth_date': date(1821, 11, 11)},
        {'first_name': 'Антон', 'last_name': 'Чехов', 'country': 'Россия', 'birth_date': date(1860, 1, 29)},
        {'first_name': 'Александр', 'last_name': 'Пушкин', 'country': 'Россия', 'birth_date': date(1799, 6, 6)},
        {'first_name': 'Михаил', 'last_name': 'Булгаков', 'country': 'Россия', 'birth_date': date(1891, 5, 15)},
        {'first_name': 'Джоан', 'last_name': 'Роулинг', 'country': 'Великобритания', 'birth_date': date(1965, 7, 31)},
        {'first_name': 'Стивен', 'last_name': 'Кинг', 'country': 'США', 'birth_date': date(1947, 9, 21)},
        {'first_name': 'Агата', 'last_name': 'Кристи', 'country': 'Великобритания', 'birth_date': date(1890, 9, 15)},
    ]
    
    authors = []
    for author_data in authors_data:
        author, created = Author.objects.get_or_create(
            first_name=author_data['first_name'],
            last_name=author_data['last_name'],
            defaults=author_data
        )
        authors.append(author)
    
    print(f"Создано авторов: {len(authors)}")
    
    # Создаем издательства
    publishers_data = [
        {'name': 'Эксмо', 'publisher_type': 'COM', 'founded_year': 1991},
        {'name': 'АСТ', 'publisher_type': 'COM', 'founded_year': 1990},
        {'name': 'Просвещение', 'publisher_type': 'STA', 'founded_year': 1930},
        {'name': 'МГУ', 'publisher_type': 'UNI', 'founded_year': 1755},
        {'name': 'Самокат', 'publisher_type': 'IND', 'founded_year': 2000},
    ]
    
    publishers = []
    for pub_data in publishers_data:
        publisher, created = Publisher.objects.get_or_create(
            name=pub_data['name'],
            defaults=pub_data
        )
        publishers.append(publisher)
    
    print(f"Создано издательств: {len(publishers)}")
    
    # Создаем книги
    books_data = [
        {'title': 'Война и мир', 'author': authors[0], 'isbn': '9785171203604', 
         'publication_date': date(2020, 1, 15), 'pages': 1274, 'price': 1200, 
         'rating': 4.8, 'genre': 'FIC', 'format': 2, 'publisher': publishers[0]},
        
        {'title': 'Преступление и наказание', 'author': authors[1], 'isbn': '9785170878858', 
         'publication_date': date(2019, 5, 20), 'pages': 608, 'price': 450, 
         'rating': 4.7, 'genre': 'FIC', 'format': 1, 'publisher': publishers[1]},
        
        {'title': 'Мастер и Маргарита', 'author': authors[4], 'isbn': '9785170937562', 
         'publication_date': date(2021, 3, 10), 'pages': 480, 'price': 550, 
         'rating': 4.9, 'genre': 'FIC', 'format': 2, 'publisher': publishers[0], 'bestseller': True},
        
        {'title': 'Евгений Онегин', 'author': authors[3], 'isbn': '9785170987650', 
         'publication_date': date(2018, 7, 5), 'pages': 320, 'price': 300, 
         'rating': 4.6, 'genre': 'FIC', 'format': 1, 'publisher': publishers[2]},
        
        {'title': 'Гарри Поттер и философский камень', 'author': authors[5], 'isbn': '9785352001307', 
         'publication_date': date(2022, 11, 25), 'pages': 432, 'price': 800, 
         'rating': 4.9, 'genre': 'FAN', 'format': 2, 'publisher': publishers[1], 'bestseller': True},
        
        {'title': 'Оно', 'author': authors[6], 'isbn': '9785170941200', 
         'publication_date': date(2020, 9, 15), 'pages': 1248, 'price': 950, 
         'rating': 4.5, 'genre': 'FAN', 'format': 1, 'publisher': publishers[0]},
        
        {'title': 'Убийство в Восточном экспрессе', 'author': authors[7], 'isbn': '9785170965251', 
         'publication_date': date(2019, 12, 1), 'pages': 320, 'price': 380, 
         'rating': 4.8, 'genre': 'MYS', 'format': 1, 'publisher': publishers[1]},
        
        {'title': 'Вишнёвый сад', 'author': authors[2], 'isbn': '9785170897453', 
         'publication_date': date(2021, 2, 14), 'pages': 128, 'price': 220, 
         'rating': 4.4, 'genre': 'FIC', 'format': 1, 'publisher': publishers[2]},
    ]
    
    books = []
    for book_data in books_data:
        book, created = Book.objects.get_or_create(
            isbn=book_data['isbn'],
            defaults=book_data
        )
        books.append(book)
    
    print(f"Создано книг: {len(books)}")
    
    # Создаем отзывы
    reviews_data = [
        {'book': books[0], 'reviewer_name': 'Алексей Петров', 'rating': 5, 
         'comment': 'Великолепная книга! Перечитываю уже в третий раз.'},
        {'book': books[1], 'reviewer_name': 'Мария Иванова', 'rating': 4, 
         'comment': 'Глубокий психологический роман, но читается тяжело.'},
        {'book': books[2], 'reviewer_name': 'Дмитрий Сидоров', 'rating': 5, 
         'comment': 'Шедевр! Обязательно к прочтению.', 'approved': True},
        {'book': books[3], 'reviewer_name': 'Елена Кузнецова', 'rating': 5, 
         'comment': 'Классика русской поэзии в прекрасном издании.', 'approved': True},
        {'book': books[4], 'reviewer_name': 'Иван Волков', 'rating': 5, 
         'comment': 'Любимая книга детства!', 'approved': True},
        {'book': books[5], 'reviewer_name': 'Ольга Смирнова', 'rating': 4, 
         'comment': 'Страшновато, но очень интересно.'},
        {'book': books[6], 'reviewer_name': 'Сергей Попов', 'rating': 5, 
         'comment': 'Лучший детектив Агаты Кристи!', 'approved': True},
        {'book': books[7], 'reviewer_name': 'Наталья Морозова', 'rating': 4, 
         'comment': 'Классическая пьеса, актуальная и сегодня.'},
    ]
    
    for review_data in reviews_data:
        Review.objects.get_or_create(
            book=review_data['book'],
            reviewer_name=review_data['reviewer_name'],
            defaults=review_data
        )
    
    print(f"Создано отзывов: {len(reviews_data)}")
    
    print("\nБаза данных успешно заполнена тестовыми данными!")
    
    # Выводим статистику
    print("\n=== СТАТИСТИКА ===")
    print(f"Всего авторов: {Author.objects.count()}")
    print(f"Всего издательств: {Publisher.objects.count()}")
    print(f"Всего книг: {Book.objects.count()}")
    print(f"Всего отзывов: {Review.objects.count()}")
    
    # Примеры запросов
    print("\n=== ПРИМЕРЫ ЗАПРОСОВ ===")
    print("1. Все книги Толстого:")
    for book in Book.objects.filter(author__last_name='Толстой'):
        print(f"   - {book.title} ({book.publication_date.year})")
    
    print("\n2. Бестселлеры:")
    for book in Book.objects.filter(bestseller=True):
        print(f"   - {book.title} - {book.price} руб.")
    
    print("\n3. Книги дороже 500 рублей:")
    expensive_books = Book.objects.filter(price__gt=500)
    print(f"   Найдено: {expensive_books.count()} книг")
    
    print("\n4. Средняя цена книг по жанрам:")
    from django.db.models import Avg
    genres = Book.objects.values('genre').annotate(avg_price=Avg('price'))
    for genre in genres:
        print(f"   {dict(Book.GenreChoices.choices)[genre['genre']]}: {genre['avg_price']:.2f} руб.")
