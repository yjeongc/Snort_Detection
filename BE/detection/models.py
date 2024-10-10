from django.db import models

class SnortAlert(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_message = models.TextField()
    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()
    protocol = models.CharField(max_length=10)

    def __str__(self):
        return self.alert_message
