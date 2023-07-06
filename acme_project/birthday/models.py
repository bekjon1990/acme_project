from django.db import models

# Импортируется функция-валидатор.
from .validators import real_age
from django.urls import reverse


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)


def get_absolute_url(self):
    # С помощью функции reverse() возвращаем URL объекта.
    return reverse('birthday:detail', kwargs={'pk': self.pk})
