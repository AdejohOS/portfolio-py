from django.db import models

from .utils_slug import slugify_instance_title
from django.db.models.signals import pre_save, post_save

import uuid
from django.urls import reverse
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    description = models.TextField(max_length=300)
    links = models.CharField(null=True, blank=True, max_length=300)
    post_image = models.ImageField(upload_to='project/post_img/', null=True, blank=True, default='default.jpg')
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_details", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        #if self.slug is None:
         #   self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def obj_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(obj_pre_save, sender=Project)


def obj_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance_title(instance, save=True)
 

post_save.connect(obj_post_save, sender=Project)



class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.tag_name


class PostImage(models.Model):
    post = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to="project/images/")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.post.title
