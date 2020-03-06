import json

from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from cashier.models import Transaction
from cashier.serializers import TransactionSerializer
from cashier.utils import calculate_banknote


@csrf_exempt
def simple_cashier(request):
    data = json.loads(request.body)
    amount_paid = data.get("amount_paid")
    amount_charged = data.get("amount_charged")
    response = calculate_banknote(amount_paid, amount_charged)

    return JsonResponse(response, status=status.HTTP_200_OK)


class TransactionView(APIView):
    @staticmethod
    def create_response(serializer):
        change = calculate_banknote(serializer.data.get('amount_paid'), serializer.data.get('amount_charged'))
        return {'transaction': serializer.data, 'change': change}

    def get(self, request, id=None, format=None):
        if id:
            transaction = Transaction.objects.filter(id=id).first()
            if not transaction:
                raise Http404

            serializer = TransactionSerializer(transaction)
            return Response(self.create_response(serializer), status=status.HTTP_200_OK)

        else:
            transactions = Transaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id=None, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.create_response(serializer), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        transaction = Transaction.objects.filter(id=id).first()
        if not transaction:
            raise Http404

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.create_response(serializer), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, format=None):
        if id is None or not Transaction.objects.filter(id=id).exists():
            return JsonResponse(
                {"Message": "Transaction doesn't exists"},
                status=status.HTTP_404_NOT_FOUND
            )

        transaction = Transaction.objects.filter(id=id).delete()
        return JsonResponse(
            {"Message": f"Transaction {id} deleted successfully"},
            status=status.HTTP_200_OK
        )
