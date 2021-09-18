from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

""""
class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #recipient = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

"""
