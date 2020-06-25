from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField()
    slug = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

    @property
    def preview(self):
        if '<p>' not in str(self.description):
            return ' '.join(str(self.description).split(' ')[:10])
        words = str(self.description).split('<p>')[1].split('</p>')[0]
        preview = ' '.join(words.split(' ')[:10])
        if len(words.split(' ')) > 10:
            preview += '.....'
        return preview
