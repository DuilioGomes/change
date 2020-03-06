from django.db import models


class Transaction(models.Model):
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_charged = models.DecimalField(max_digits=10, decimal_places=2)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'date: {self.create_date}'
