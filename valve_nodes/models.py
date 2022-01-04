from django.db import models
from django.shortcuts import reverse
from slugify import slugify
from time import time


def slug_gen(s):
    new_slug = slugify(s)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    text = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    """
    Класс для группировки объектов по отношениям, группа, местонахождению, установке.
    """
    title = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)


'''
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.book.title)


class MeterDevice:
    # Перечислить базовые характеристики СИ
    # Наследовать не нужно! отношения только тегами


class MeterInstance(models.Model):
    pass
'''


class ValveNode(models.Model):
    STATUS = (
        ('m', 'Техническое обслуживание'),
        ('o', 'Эксплуатация'),
        ('d', 'Выведен из эксплуатации'),
        ('r', 'Зарезервировано'),
    )

    title = models.CharField('Наименование', max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    locate = models.CharField('Расположение', blank=True, max_length=50, null=True, help_text='Введите местонахождение объекта')
    node_state = models.CharField('Статус',choices=STATUS, default='o', blank=True, max_length=50, null=True,
                                  help_text="Введите статус КУ (Эксплуатация, Ремонт, Отключен")
    visit_date = models.DateField('Последний визит', blank=True, null=True)
    visit_master = models.CharField('Последние посетившие', max_length=100, blank=True)  # neeed many to many
    note = models.TextField('Комментарии', blank=True, null=True, help_text='Enter Note')
    tags = models.ManyToManyField('Tag', blank=True, related_name='valve_nodes',
                                  help_text='Отметьте отношения к объектам')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_gen(self.title)
        super(ValveNode, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model.
        Django автоматически добавит кнопку «Просмотр на сайте» на экранах редактирования записей модели
         на сайте администратора)"""
        return reverse('valve_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('valve_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('valve_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class MeterDevice(models.Model):
    title = models.CharField(max_length=80, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    device_type = models.CharField(max_length=80, blank=True, help_text='Тип СИ')
    state = models.CharField(max_length=50, blank=True, null=True, help_text='состояние, уст, хранение, ремонт, утиль')
    place = models.CharField(max_length=50, blank=True, null=True, help_text='Место нахождения')
    tags = models.ManyToManyField('Tag', blank=True, related_name='meter_devices')
    tag_name = models.CharField(max_length=100, blank=True, null=True, help_text='Содержимое бирки')
    tag_check = models.BooleanField(help_text='Бирка установлена', null=True)
    number_factory = models.CharField(max_length=20, blank=True, null=True, help_text='Заводской номер')
    model = models.CharField(max_length=50, blank=True, null=True, help_text='Модель')
    meter_limit = models.CharField(max_length=50, blank=True, null=True, help_text='Предел измерений')
    accuracy = models.CharField(max_length=10, blank=True, null=True, help_text='Класс точности')
    date_make = models.DateField('Дата производства', blank=True, null=True)
    date_verify_mark = models.DateField('Дата поверки-калибровки', blank=True, null=True)
    date_install = models.DateField('Дата установки', blank=True, null=True)
    date_uninstall = models.DateField('Дата снятия', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model.
        Django автоматически добавит кнопку «Просмотр на сайте» на экранах редактирования записей модели
         на сайте администратора)"""
        return reverse('meter_detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('meter_update', kwargs={'slug': self.slug})
