import pandas as pd


async def convert_rubles_to_other_currency(cur):
    tables = pd.read_html('https://cbr.ru/currency_base/daily/', decimal=',', thousands='.')
    table = tables[0]
    table.rename(columns={'Цифр. код': 'digit_code', 'Букв. код': 'letter_code', 'Валюта': 'currency', 'Курс': 'course',
                          'Единиц': 'count'}, inplace=True)

    return float(table.loc[table.letter_code == cur].course.values[0])
