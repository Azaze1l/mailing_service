from django.db import models


class Mailing(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    message_text = models.CharField(max_length=400)
    tag_filter = models.CharField(max_length=15)
    mobile_code_filter = models.IntegerField()


class Recipient(models.Model):
    """TODO: move constant to somewhere"""
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone = models.IntegerField()
    mobile_code = models.IntegerField()
    tag = models.CharField(max_length=15)
    timezone = models.CharField(max_length=32, choices=TIMEZONES)


class Message(models.Model):
    sent_at = models.DateTimeField()
    status = models.IntegerField()
    mailing_id = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    recipient_id = models.ForeignKey(Recipient, on_delete=models.CASCADE)


