from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Копия оригинальной модели с добавлением нового поля
# ... (весь предыдущий код моделей) ...

# В классе Book добавляем новое поле после 'price':
#     discount_price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         verbose_name="Цена со скидкой",
#         null=True,
#         blank=True,
#         validators=[MinValueValidator(0)]
#     )
