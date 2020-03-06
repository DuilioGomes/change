# import decimal
import json
from decimal import Decimal


def calculate_banknote(amount_paid, amount_charged):
    try:
        if type(amount_paid) is str:
            amount_paid = amount_paid.replace(',', '.')
        if type(amount_charged) is str:
            amount_charged = amount_charged.replace(',', '.')

        amount_charged = round(Decimal(amount_charged), 2)
        amount_paid = round(Decimal(amount_paid), 2)
    except Exception as e:
        raise Exception

    change = amount_paid - amount_charged

    banknote = {"R100": change // Decimal('100')}
    aux = change % Decimal('100')

    banknote["R50"] = aux // Decimal('50')
    aux = aux % Decimal('50')

    banknote["R10"] = aux // Decimal('10')
    aux = aux % Decimal('10')

    banknote["R5"] = aux // Decimal('5')
    aux = aux % Decimal('5')

    banknote["R1"] = aux // Decimal('1')
    aux = aux % Decimal('1')

    banknote["R0.5"] = aux // Decimal('0.5')
    aux = aux % Decimal('0.5')

    banknote["R0.1"] = aux // Decimal('0.1')
    aux = aux % Decimal('0.1')

    banknote["R0.05"] = aux // Decimal('0.05')
    aux = aux % Decimal('0.05')

    banknote["R0.01"] = aux // Decimal('0.01')
    response = {'banknotes': banknote, 'amount_paid': amount_paid, 'amount_charged': amount_charged, 'change': change}

    return json.loads(json.dumps(response, cls=DecimalEncoder))


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
