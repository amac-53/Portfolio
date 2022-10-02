# Generated by Django 4.1.1 on 2022-10-01 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100, verbose_name='コース')),
                ('school', models.CharField(max_length=100, verbose_name='学校')),
                ('period', models.CharField(max_length=100, verbose_name='期間')),
                ('description', models.TextField(verbose_name='説明')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='タイトル')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='サブタイトル')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('job', models.TextField(verbose_name='仕事')),
                ('introduction', models.TextField(verbose_name='自己紹介')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='github')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='instagram')),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True, verbose_name='linkedin')),
                ('topimage', models.ImageField(upload_to='images', verbose_name='トップ画像')),
                ('subimage', models.ImageField(upload_to='images', verbose_name='サブ画像')),
            ],
        ),
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='言語名')),
                ('image', models.FileField(upload_to='images', verbose_name='アイコン画像')),
                ('level', models.CharField(max_length=100, verbose_name='レベル')),
                ('percentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='パーセンテージ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='レベルの説明')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ソフトウェア')),
                ('image', models.FileField(upload_to='images', verbose_name='アイコン画像')),
                ('level', models.CharField(max_length=100, verbose_name='レベル')),
                ('percentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='パーセンテージ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='レベルの説明')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('image', models.ImageField(upload_to='images', verbose_name='イメージ画像')),
                ('thumbnail', models.ImageField(null=True, upload_to='images', verbose_name='サムネイル')),
                ('skill', models.CharField(max_length=255, verbose_name='スキル')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL')),
                ('created', models.DateField(verbose_name='作成日')),
                ('description', models.TextField(verbose_name='説明')),
            ],
        ),
    ]
