from sanic.response import json
from sanic import Sanic

from get_amount_target_currency import get_amount_target_currency
from parser_currency_rate import convert_rubles_to_other_currency

app = Sanic('CurrencyConverter')


@app.get('/api/course/<currency:string>')
async def get_currency_rate_against_ruble(request, currency: str):
    rub_course = await convert_rubles_to_other_currency(currency)
    return json({'currency': currency, 'rub_course': rub_course})


@app.post('/api/convert')
async def convert_from_one_currency_to_another(request):
    from_currency = request.json.get('from_currency')
    to_currency = request.json.get('to_currency')
    amount_original_currency = request.json.get('amount')

    amount_target_currency = await get_amount_target_currency(from_currency, to_currency, amount_original_currency)

    return json({'currency': to_currency, 'amount': amount_target_currency})


if __name__ == '__main__':
    app.run()
