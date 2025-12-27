from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db.models import Q

class Author(models.Model):
    """Модель автора книги"""
    
    # Валидатор для имени и фамилии
    name_validator = RegexValidator(
        regex=r'^[A-Za-zА-Яа-яЁё\s\-]+$',  # Исправлено: добавлен r перед строкой
        message='Имя может содержать только буквы, пробелы и дефисы'
    )
    
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        validators=[name_validator]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
        validators=[name_validator]
    )
    email = models.EmailField(
        verbose_name="Email",
        blank=True,
        null=True
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        null=True,
        blank=True
    )
    country = models.CharField(
        max_length=100,
        verbose_name="Страна",
        default="Не указана"
    )
    biography = models.TextField(
        verbose_name="Биография",
        blank=True,
        default=""
    )
    is_active = models.BooleanField(
        verbose_name="Активный автор",
        default=True
    )
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['last_name', 'first_name']
        unique_together = [['first_name', 'last_name', 'birth_date']]
        indexes = [
            models.Index(fields=['last_name']),
            models.Index(fields=['country']),
        ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.last_name}, {self.first_name}"

class Publisher(models.Model):
    """Модель издательства"""
    
    class PublisherTypes(models.TextChoices):
        COMMERCIAL = 'COM', 'Коммерческое'
        STATE = 'STA', 'Государственное'
        UNIVERSITY = 'UNI', 'Университетское'
        INDEPENDENT = 'IND', 'Независимое'
    
    name = models.CharField(
        max_length=200,
        verbose_name="Название издательства",
        unique=True
    )
    publisher_type = models.CharField(
        max_length=3,
        choices=PublisherTypes.choices,
        default=PublisherTypes.COMMERCIAL,
        verbose_name="Тип издательства"
    )
    founded_year = models.PositiveIntegerField(
        verbose_name="Год основания",
        validators=[
            MinValueValidator(1500),
            MaxValueValidator(2024)
        ]
    )
    address = models.TextField(
        verbose_name="Адрес",
        blank=True
    )
    website = models.URLField(
        verbose_name="Веб-сайт",
        blank=True
    )
    email = models.EmailField(
        verbose_name="Контактный email",
        blank=True
    )
    
    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.get_publisher_type_display()})"

class Book(models.Model):
    """Модель книги"""
    
    class GenreChoices(models.TextChoices):
        FICTION = 'FIC', 'Художественная литература'
        NON_FICTION = 'NON', 'Нехудожественная литература'
        SCI_FI = 'SFI', 'Научная фантастика'
        FANTASY = 'FAN', 'Фэнтези'
        MYSTERY = 'MYS', 'Детектив'
        ROMANCE = 'ROM', 'Роман'
        BIOGRAPHY = 'BIO', 'Биография'
        HISTORY = 'HIS', 'История'
        SCIENCE = 'SCI', 'Наука'
    
    class FormatChoices(models.IntegerChoices):
        PAPERBACK = 1, 'Мягкая обложка'
        HARDCOVER = 2, 'Твердая обложка'
        EBOOK = 3, 'Электронная книга'
        AUDIOBOOK = 4, 'Аудиокнига'
    
    # Основные поля
    title = models.CharField(
        max_length=300,
        verbose_name="Название книги",
        db_index=True
    )
    
    # Связи
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name='books'
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Издательство",
        related_name='published_books'
    )
    
    # Информация о книге
    isbn = models.CharField(
        max_length=17,
        verbose_name="ISBN",
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^(97(8|9))?\d{9}(\d|X)$',  # Исправлено: добавлен r
                message='Введите корректный ISBN (10 или 13 цифр)'
            )
        ]
    )
    publication_date = models.DateField(
        verbose_name="Дата публикации"
    )
    pages = models.PositiveIntegerField(
        verbose_name="Количество страниц",
        validators=[MinValueValidator(1)]
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        validators=[MinValueValidator(0)]
    )
    rating = models.FloatField(
        verbose_name="Рейтинг",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=0,
        blank=True
    )
    
    # Категории
    genre = models.CharField(
        max_length=3,
        choices=GenreChoices.choices,
        default=GenreChoices.FICTION,
        verbose_name="Жанр"
    )
    format = models.IntegerField(
        choices=FormatChoices.choices,
        default=FormatChoices.PAPERBACK,
        verbose_name="Формат"
    )
    
    # Описание и статус
    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )
    available = models.BooleanField(
        verbose_name="В наличии",
        default=True
    )
    bestseller = models.BooleanField(
        verbose_name="Бестселлер",
        default=False
    )
    
    # Технические поля
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True
    )
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['-publication_date', 'title']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['genre', 'format']),
            models.Index(fields=['price']),
            models.Index(fields=['rating']),
        ]
        constraints = [
            # Исправлено для Django 6.0
            models.CheckConstraint(
                condition=models.Q(pages__gt=0),  # Исправлено: condition вместо check
                name='pages_must_be_positive'
            ),
            models.CheckConstraint(
                condition=models.Q(price__gte=0),
                name='price_cannot_be_negative'
            ),
            models.CheckConstraint(
                condition=models.Q(rating__gte=0) & models.Q(rating__lte=10),
                name='rating_range_0_to_10'
            ),
            models.UniqueConstraint(
                fields=['title', 'author', 'publication_date'],
                name='unique_book_edition'
            ),
        ]
    
    def __str__(self):
        return f"{self.title} ({self.author})"
    
    @property
    def price_with_vat(self):
        """Цена с НДС (20%)"""
        return round(float(self.price) * 1.2, 2)
    
    @property
    def is_new(self):
        """Книга считается новой, если издана в текущем году"""
        from datetime import date
        return self.publication_date.year == date.today().year
    
    @property
    def page_price_ratio(self):
        """Цена за страницу"""
        if self.pages > 0:
            return round(float(self.price) / self.pages, 4)
        return 0

class Review(models.Model):
    """Модель отзыва на книгу"""
    
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга",
        related_name='reviews'
    )
    reviewer_name = models.CharField(
        max_length=100,
        verbose_name="Имя рецензента"
    )
    email = models.EmailField(
        verbose_name="Email рецензента",
        blank=True
    )
    rating = models.IntegerField(
        verbose_name="Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(
        verbose_name="Текст отзыва",
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name="Дата отзыва",
        auto_now_add=True
    )
    approved = models.BooleanField(
        verbose_name="Одобрен",
        default=False
    )
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['book', 'rating']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f"Отзыв на '{self.book.title}' от {self.reviewer_name}"
