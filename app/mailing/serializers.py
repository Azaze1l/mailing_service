from rest_framework import serializers
from .models import Mailing, Message, Recipient


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = [
            'id',
            'start_datetime',
            'end_datetime',
            'message_text',
            'tag_filter',
            'mobile_code_filter',
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'sent_at',
            'status',
            'mailing_id',
            'recipient_id',
        ]


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = [
            'id',
            'phone',
            'mobile_code',
            'tag',
            'timezone',
        ]
