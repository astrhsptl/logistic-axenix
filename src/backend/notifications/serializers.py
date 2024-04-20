
from rest_framework.serializers import ModelSerializer
from .models import Notification

class NotificationModelSerializer(ModelSerializer):

    class Meta:
        model = Notification
        fields = "__all__"