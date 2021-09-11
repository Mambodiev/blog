from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })

    def get_like_url(self):
        return reverse("like", kwargs={
            'slug': self.slug
        })

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class About(models.Model):
    name = models.CharField(max_length=50)
    about_text = RichTextUploadingField()
    
    def __str__(self):
        return self.about_text


class PrivacyPolicy(models.Model):
    name = models.CharField(max_length=50)
    privacy_policy_text = RichTextUploadingField(blank=True, null=True,)
    
    class Meta:
        verbose_name_plural = "Privacy Policies"

    def __str__(self):
        return self.privacy_policy_text


class TermsOfUse(models.Model):
    name = models.CharField(max_length=50)
    terms_of_use_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.terms_of_use_text
