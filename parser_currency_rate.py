import pandas as pd

URL_CB = 'https://cbr.ru/currency_base/daily/'


async def parsing_data_currency_rates():
    parsed_data_from_site = pd.read_html(URL_CB, decimal=',', thousands='.')
    parsed_data_currency_rates = parsed_data_from_site[0]
    parsed_data_currency_rates.rename(
        columns={'Цифр. код': 'digit_code', 'Букв. код': 'letter_code', 'Валюта': 'currency',
                 'Курс': 'course', 'Единиц': 'count'},
        inplace=True
    )
    return parsed_data_currency_rates


async def convert_rubles_to_other_currency(currency):
    currency_rates_data = await parsing_data_currency_rates()
    raw_data_with_selected_currency = currency_rates_data.loc[currency_rates_data.letter_code == currency]
    value_course = raw_data_with_selected_currency.course.values[0]
    return float(value_course)


async def get_list_letters_code_currency():
    currency_rates_data = await parsing_data_currency_rates()
    list_letters_code_currency = list(currency_rates_data.letter_code) + ['RUB']
    return list_letters_code_currency

