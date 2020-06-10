from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField()
    slug = models.SlugField(max_length=32, unique=True)

    def __str__(self):
        return self.title

    @property
    def preview(self):
        words = str(self.content).split(' ')
        preview = ' '.join(words[:100])
        if len(words) > 100:
            preview += '...'
        return preview
