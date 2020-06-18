from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=64)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    creation_date = models.DateTimeField()
    slug = models.SlugField(max_length=32, unique=True)

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        return ', '.join([t.name for t in self.tags.all()])

    @property
    def preview(self):
        if '<p>' not in str(self.content):
            return ' '.join(str(self.content).split(' ')[:50])
        words = str(self.content).split('<p>')[1].split('</p>')[0]
        preview = ' '.join(words.split(' ')[:50])
        if preview[-1] == '.':
            preview += '..'
        else:
            preview += '...'
        return preview
