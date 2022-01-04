# Generated by Django 4.0 on 2022-01-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValveNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=80)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('locate', models.CharField(blank=True, help_text='Введите местонахождение объекта', max_length=50, null=True)),
                ('node_state', models.CharField(blank=True, help_text='Введите статус КУ (Эксплуатация, Ремонт, Отключен', max_length=50, null=True)),
                ('visit_date', models.DateField(blank=True, null=True)),
                ('visit_master', models.CharField(blank=True, help_text='Посетившие работники', max_length=100)),
                ('note', models.TextField(blank=True, help_text='Enter Note', null=True)),
                ('tags', models.ManyToManyField(blank=True, help_text='Отметьте отношения к объектам', related_name='valve_nodes', to='valve_nodes.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('text', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='valve_nodes.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='MeterDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=80)),
                ('device_type', models.CharField(blank=True, help_text='Тип СИ', max_length=80)),
                ('state', models.CharField(blank=True, help_text='состояние, уст, хранение, ремонт, утиль', max_length=50, null=True)),
                ('place', models.CharField(blank=True, help_text='Место нахождения', max_length=50, null=True)),
                ('tag_name', models.CharField(blank=True, help_text='Содержимое бирки', max_length=100, null=True)),
                ('tag_check', models.BooleanField(help_text='Бирка установлена', null=True)),
                ('number_factory', models.CharField(blank=True, help_text='Заводской номер', max_length=20, null=True)),
                ('model', models.CharField(blank=True, help_text='Модель', max_length=50, null=True)),
                ('meter_limit', models.CharField(blank=True, help_text='Предел измерений', max_length=50, null=True)),
                ('accuracy', models.CharField(blank=True, help_text='Класс точности', max_length=10, null=True)),
                ('date_make', models.DateField(blank=True, null=True, verbose_name='Дата производства')),
                ('date_verify_mark', models.DateField(blank=True, null=True, verbose_name='Дата поверки-калибровки')),
                ('date_install', models.DateField(blank=True, null=True, verbose_name='Дата установки')),
                ('date_uninstall', models.DateField(blank=True, null=True, verbose_name='Дата снятия')),
                ('tags', models.ManyToManyField(blank=True, related_name='meter_devices', to='valve_nodes.Tag')),
            ],
        ),
    ]