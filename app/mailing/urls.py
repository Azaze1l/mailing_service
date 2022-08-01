
from django.urls import path
from . import views


urlpatterns = [
    path(
        'recipient/<int:pk>/',
        views.RetrieveUpdateDestroyRecipientAPIView.as_view(),
        name='get_delete_update_recipient',
    ),
    path(
        'mailing/<int:pk>/',
        views.RetrieveUpdateDestroyMailingAPIView.as_view(),
        name='get_delete_update_mailing',
    ),
]
