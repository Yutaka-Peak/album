from django.db import models

# Create your models here.
class AlbumModel(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image_01 = models.ImageField(upload_to='')
    memo_01 = models.TextField()

    image_02 = models.ImageField(upload_to='')
    memo_02 = models.TextField()

    image_03 = models.ImageField(upload_to='')
    memo_03 = models.TextField()

    image_04 = models.ImageField(upload_to='')
    memo_04 = models.TextField()

    image_05 = models.ImageField(upload_to='')
    memo_05 = models.TextField()

    image_06 = models.ImageField(upload_to='')
    memo_06 = models.TextField()

    image_07 = models.ImageField(upload_to='')
    memo_07 = models.TextField()

    image_08 = models.ImageField(upload_to='')
    memo_08 = models.TextField()

    image_09 = models.ImageField(upload_to='')
    memo_09 = models.TextField()

    image_10 = models.ImageField(upload_to='')
    memo_10 = models.TextField()

    update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

