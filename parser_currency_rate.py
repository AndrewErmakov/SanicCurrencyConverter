import pandas as pd

URL_CB = 'https://cbr.ru/currency_base/daily/'


async def convert_rubles_to_other_currency(currency):
    parsed_data_from_site = pd.read_html(URL_CB, decimal=',', thousands='.')
    parsed_data_currency_rates = parsed_data_from_site[0]
    parsed_data_currency_rates.rename(
        columns={'Цифр. код': 'digit_code', 'Букв. код': 'letter_code', 'Валюта': 'currency',
                 'Курс': 'course', 'Единиц': 'count'},
        inplace=True
    )
    raw_data_with_selected_currency = parsed_data_currency_rates.loc[parsed_data_currency_rates.letter_code == currency]
    value_course = raw_data_with_selected_currency.course.values[0]
    return float(value_course)
