from sanic.response import json
from sanic import Sanic
from converter import convert_rubles_to_other_currency

app = Sanic('CurrencyConverter')


@app.get('/api/course/<currency:string>')
async def get_currency_rate(request, currency: str):
    rub_course = await convert_rubles_to_other_currency(currency)
    return json({'currency': currency, 'rub_course': rub_course})


@app.post('/api/convert')
async def how_much_rubles(request):
    from_currency = request.json.get('from_currency')
    to_currency = request.json.get('to_currency')
    amount = request.json.get('amount')

    if to_currency == 'RUB':
        amount = amount * await convert_rubles_to_other_currency(from_currency)
    else:
        original_currency_against_ruble = await convert_rubles_to_other_currency(from_currency)
        target_currency_against_ruble = await convert_rubles_to_other_currency(to_currency)

        target_currency_rate_relative_to_the_original = original_currency_against_ruble / target_currency_against_ruble
        amount = amount * target_currency_rate_relative_to_the_original

    return json({'currency': to_currency,
                 'amount': amount})


if __name__ == '__main__':
    app.run()
