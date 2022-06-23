from django.db import models
from django.utils import timezone


class Entry(models.Model):
    created_on = models.DateField()
    updated_on = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_on = timezone.now().date()
        self.updated_on = timezone.now().date()
        return super(Entry, self).save(*args, **kwargs)

    class Meta:
        get_latest_by = ['created_on', ]
        ordering = ['-created_on']
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.title
