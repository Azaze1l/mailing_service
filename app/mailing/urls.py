from django.urls import path
from . import views

urlpatterns = [
    path(
        'recipient/<int:pk>/',
        views.UpdateDestroyRecipientAPIView.as_view(),
        name='delete_update_recipient',
    ),
    path(
        'recipient/',
        views.CreateRecipientAPIView.as_view(),
        name='create_recipient',
    ),
    path(
        'mailing/<int:pk>/',
        views.UpdateDestroyMailingAPIView.as_view(),
        name='delete_update_mailing',
    ),
    path(
        'mailing/',
        views.CreateMailingAPIView.as_view(),
        name='create_mailing',
    ),
    path('test/',
         views.TestProcessing.as_view(),
         name='create_mailing')
]
