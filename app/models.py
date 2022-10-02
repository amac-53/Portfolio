from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True) 
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    linkedin = models.CharField('linkedin', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name


class Work(models.Model):
    """
    作品用データ
    """

    title = models.CharField('タイトル', max_length=255)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True)
    skill = models.CharField('スキル', max_length=255)
    url = models.CharField('URL', max_length=255, null=True, blank=True)
    created = models.DateField('作成日')
    description = models.TextField('説明')

    def __str__(self):
        return self.title


class Education(models.Model):
    """
    学歴用
    """
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    period = models.CharField('期間', max_length=100)
    description = models.TextField('説明')

    def __str__(self):
        return self.course

class Software(models.Model):
    """
    ソフトウェア用
    """
    name = models.CharField('ソフトウェア', max_length=100)
    image = models.FileField(upload_to='images', verbose_name='アイコン画像')
    level = models.CharField('レベル', max_length=100)
    percentage = models.PositiveIntegerField('パーセンテージ', validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField('レベルの説明', blank=True, null=True)

    def __str__(self):
        return self.name


class Programming(models.Model):
    """
    プログラミング言語用
    """
    name = models.CharField('言語名', max_length=100)
    image = models.FileField(upload_to='images', verbose_name='アイコン画像')
    level = models.CharField('レベル', max_length=100)
    percentage = models.PositiveIntegerField('パーセンテージ', validators=[MinValueValidator(1), MaxValueValidator(100)])
    description = models.TextField('レベルの説明', blank=True, null=True)

    def __str__(self):
        return self.name
