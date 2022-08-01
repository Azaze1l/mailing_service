from rest_framework import mixins
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from .models import Recipient, Mailing
from .serializers import RecipientSerializer, MailingSerializer


class RetrieveUpdateDestroyRecipientAPIView(CreateAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = RecipientSerializer
    queryset = Recipient.objects.all()
    permission_classes = [AllowAny]


class RetrieveUpdateDestroyMailingAPIView(CreateAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()
    permission_classes = [AllowAny]
