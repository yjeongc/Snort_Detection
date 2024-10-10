from django.db import models

class SnortAlert(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_message = models.CharField(max_length=255)
    source_ip = models.CharField(max_length=15)
    destination_ip = models.CharField(max_length=15)
    protocol = models.CharField(max_length=10)

    def __str__(self):
        return self.alert_message

