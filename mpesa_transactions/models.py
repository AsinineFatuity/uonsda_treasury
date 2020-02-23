from django.db import models


# Create your models here.
class BaseTransactions(models.Model):
    transaction_choices = [
        ('C', 'Completed'),
        ('I', 'Incompleted'),
    ]
    transaction_status = models.CharField(max_length=20, choices=transaction_choices)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Transaction(BaseTransactions):
    reason_choices = [
        ('P','Pay utility'),
        ('O','Pay Utility with OD via sdk'),
    ]
    paid_in  = models.IntegerField()
    withdrawn = models.IntegerField()
    balance = models.IntegerField()
    balance_confirmed = models.BooleanField()
    reason_type = models.CharField(max_length=20,choices=reason_choices)
    other_party_no = models.CharField(max_length=200,null=True)
    linked  = models.BooleanField()
    account_no = models.CharField(max_length=200,null=True)