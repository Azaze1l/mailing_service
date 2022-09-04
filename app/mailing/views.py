from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Recipient, Mailing
from .serializers import RecipientSerializer, MailingSerializer


class UpdateDestroyRecipientAPIView(UpdateAPIView, DestroyAPIView):
    serializer_class = RecipientSerializer
    queryset = Recipient.objects.all()
    permission_classes = [AllowAny]


class CreateRecipientAPIView(CreateAPIView):
    serializer_class = RecipientSerializer
    queryset = Recipient.objects.all()
    permission_classes = [AllowAny]


class UpdateDestroyMailingAPIView(UpdateAPIView, DestroyAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()
    permission_classes = [AllowAny]


class CreateMailingAPIView(CreateAPIView):
    serializer_class = MailingSerializer
    queryset = Recipient.objects.all()
    permission_classes = [AllowAny]


class TestProcessing(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        relevant_mailings_objects = Mailing.objects.filter(end_datetime=None)
        print(MailingSerializer(relevant_mailings_objects))
        return JsonResponse({'code': 200,'data': ""}, status=200)
