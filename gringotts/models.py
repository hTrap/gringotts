from django.db import models


REQUEST_CHOICES = [
    ('get', 'GET Request'),
    ('post', 'POST Request')]


class API(models.Model):
    api_name = models.CharField(max_length=30)
    api_version = models.CharField(max_length=30)
    transaction = models.ForeignKey('Transaction', null=True, blank=True,
                                    related_name='transactions')


class Transaction(models.Model):
    request_type = models.CharField(choices=REQUEST_CHOICES, max_length=10)
    request_body = models.CharField(max_length=180)
