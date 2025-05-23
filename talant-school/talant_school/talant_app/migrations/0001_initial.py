# Generated by Django 5.1.7 on 2025-03-17 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text1', models.TextField(verbose_name='Первый абзац')),
                ('text2', models.TextField(verbose_name='Второй абзац')),
                ('image', models.ImageField(upload_to='about/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='AdministrationMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('position', models.CharField(max_length=200, verbose_name='Должность')),
                ('photo', models.ImageField(upload_to='administration/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Член администрации',
                'verbose_name_plural': 'Администрация',
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название клуба')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='clubs/', verbose_name='Основное изображение')),
                ('leader', models.CharField(max_length=100, verbose_name='Руководитель')),
                ('schedule', models.CharField(help_text='Например: Пн, Ср 15:00-16:30', max_length=200, verbose_name='Расписание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Клуб',
                'verbose_name_plural': 'Клубы',
            },
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название уровня')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='education/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Уровень образования',
                'verbose_name_plural': 'Уровни образования',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Регистрация',
                'verbose_name_plural': 'Регистрации',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('link_text', models.CharField(max_length=100, verbose_name='Текст ссылки')),
                ('link_url', models.URLField(verbose_name='URL ссылки')),
                ('background_image', models.ImageField(upload_to='slider/', verbose_name='Фоновое изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.CreateModel(
            name='ClubImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='club_gallery/', verbose_name='Изображение')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='talant_app.club')),
            ],
            options={
                'verbose_name': 'Изображение клуба',
                'verbose_name_plural': 'Изображения клуба',
            },
        ),
    ]
