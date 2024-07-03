from django.db import models

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.room_name
    


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True, related_name='messages')
    sender = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, max_length=255, null=True)


    def __str__(self):
        return self.sender + ": " + self.message