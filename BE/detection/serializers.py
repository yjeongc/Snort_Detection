from rest_framework import serializers
from .models import SnortAlert

class SnortAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnortAlert
        fields = ['id', 'timestamp', 'alert_message', 'source_ip', 'destination_ip', 'protocol']
