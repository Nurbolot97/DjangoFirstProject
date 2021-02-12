from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, 
        self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, 
                                on_delete=models.CASCADE, 
                                related_name='posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, 
                            choices=STATUS_CHOICES, 
                            default='draft')
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    objects = models.Manager()
    published = models.Manager()


    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year,
                                            self.publish.month,
                                            self.publish.day,
                                            self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                                    related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                    related_name='users_comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Comments by {self.author} on {self.post}"























