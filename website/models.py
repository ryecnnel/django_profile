from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    timestamp = models.DateTimeField(
        null=True, 
        auto_now_add=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True)

    timestamp = models.DateTimeField(
        null = True, 
        auto_now_add=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)
    
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
        
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
        
    body = models.TextField(
        blank=True,
        null=False)
        
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)
        
    tags = models.ManyToManyField(
        Tag,
        blank=True)
    
    description = models.TextField(blank=True)
    published = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if self.is_public and not self.published:
            self.published = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title