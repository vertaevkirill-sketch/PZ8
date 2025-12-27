from django.contrib import admin
from django.utils.html import format_html
from .models import Author, Publisher, Book, Review

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'country', 'birth_date', 'is_active']
    list_filter = ['country', 'is_active', 'birth_date']
    search_fields = ['first_name', 'last_name', 'email']
    list_editable = ['is_active']
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'birth_date', 'country')
        }),
        ('Контактная информация', {
            'fields': ('email',)
        }),
        ('Дополнительно', {
            'fields': ('biography', 'is_active')
        }),
    )
    readonly_fields = ['full_name']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'publisher_type', 'founded_year', 'website_link']
    list_filter = ['publisher_type', 'founded_year']
    search_fields = ['name', 'address']
    
    def website_link(self, obj):
        if obj.website:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.website, 'Сайт')
        return "Нет сайта"
    website_link.short_description = "Веб-сайт"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher', 'price', 'genre_display', 
                    'format_display', 'available', 'bestseller', 'price_with_vat']
    list_filter = ['genre', 'format', 'available', 'bestseller', 'publication_date']
    search_fields = ['title', 'isbn', 'author__first_name', 'author__last_name']
    list_editable = ['available', 'bestseller']
    readonly_fields = ['created_at', 'updated_at', 'is_new', 'page_price_ratio']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'author', 'publisher', 'isbn')
        }),
        ('Детали книги', {
            'fields': ('publication_date', 'pages', 'price', 'rating', 
                      'genre', 'format', 'description')
        }),
        ('Статус', {
            'fields': ('available', 'bestseller')
        }),
        ('Техническая информация', {
            'fields': ('created_at', 'updated_at', 'is_new', 'page_price_ratio')
        }),
    )
    
    def genre_display(self, obj):
        return obj.get_genre_display()
    genre_display.short_description = "Жанр"
    
    def format_display(self, obj):
        return obj.get_format_display()
    format_display.short_description = "Формат"
    
    def price_with_vat(self, obj):
        return f"{obj.price_with_vat} руб."
    price_with_vat.short_description = "Цена с НДС"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'reviewer_name', 'rating', 'approved', 'created_at']
    list_filter = ['rating', 'approved', 'created_at']
    search_fields = ['reviewer_name', 'book__title', 'comment']
    list_editable = ['approved']
    readonly_fields = ['created_at']
