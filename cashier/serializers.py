from rest_framework import serializers

from cashier.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount_paid', 'amount_charged', 'update_date', 'create_date']
