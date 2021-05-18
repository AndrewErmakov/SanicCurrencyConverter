from parser_currency_rate import convert_rubles_to_other_currency


async def get_amount_target_currency(original_currency, target_currency, amount_original_currency):
    if target_currency == original_currency == 'RUB':
        amount_target_currency = amount_original_currency
    elif target_currency == 'RUB':
        amount_target_currency = amount_original_currency * await convert_rubles_to_other_currency(original_currency)
    elif original_currency == 'RUB':
        amount_target_currency = amount_original_currency / await convert_rubles_to_other_currency(target_currency)
    else:
        original_currency_against_ruble = await convert_rubles_to_other_currency(original_currency)
        target_currency_against_ruble = await convert_rubles_to_other_currency(target_currency)

        target_currency_rate_relative_to_the_original = original_currency_against_ruble / target_currency_against_ruble
        amount_target_currency = amount_original_currency * target_currency_rate_relative_to_the_original

    return amount_target_currency
