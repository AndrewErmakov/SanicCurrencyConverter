from sanic.response import json
from sanic import Sanic

from get_amount_target_currency import get_amount_target_currency
from parser_currency_rate import convert_rubles_to_other_currency
from validate_json_data import validate_get_request, validate_json_data_post_request

app = Sanic('CurrencyConverter')


@app.get('/api/course/<currency:string>')
async def get_currency_rate_against_ruble(request, currency: str):
    # validate currency from list letters code currency
    result_validation = await validate_get_request(currency)
    if not result_validation:
        return json({'success': False}, status=421)

    # if validation passed
    rub_course = await convert_rubles_to_other_currency(currency)
    return json({'currency': currency, 'rub_course': rub_course}, status=200)


@app.post('/api/convert')
async def convert_from_one_currency_to_another(request):
    # validation json data
    result_validation_json = await validate_json_data_post_request(request.json)
    if not result_validation_json:
        return json({'success': False}, status=421)

    # if validation passed
    from_currency = request.json.get('from_currency')
    to_currency = request.json.get('to_currency')
    amount_original_currency = request.json.get('amount')

    amount_target_currency = await get_amount_target_currency(from_currency, to_currency, amount_original_currency)

    return json({'currency': to_currency, 'amount': amount_target_currency}, status=201)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
