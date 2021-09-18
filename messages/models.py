from django.db import models

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
