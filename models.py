from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Category(models.Model):
  name = models.CharField('カテゴリ', max_length=100)

  def __str__(self):
    return self.name

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
  title = models.CharField("タイトル", max_length=200)
  image = models.ImageField(upload_to='image', verbose_name='イメージ画像', null=True, blank=True)
  content = models.TextField("本文")
  created = models.DateTimeField("作成日", default=timezone.now)

  def __str__(self):
    return self.title