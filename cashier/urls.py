from django.urls import path
from cashier.views import simple_cashier, TransactionView

urlpatterns = {
    path('simple_cashier', simple_cashier, name='simple_cashier'),
    path('transaction', TransactionView.as_view(), name='transactions'),
    path('transaction/<int:id>', TransactionView.as_view(), name='transactions'),
}
