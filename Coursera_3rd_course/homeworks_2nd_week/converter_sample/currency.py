from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, date, requests):
    url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req="
    response = requests.get(url+date)  # Использовать переданный requests
    soup = BeautifulSoup(response.text, 'lxml')

    if cur_from == 'RUR':
        nominal_2 = Decimal(soup.find("charcode", text=cur_to).find_next_sibling('nominal').string.replace(',', '.'))
        value_2 = Decimal(soup.find("charcode", text=cur_to).find_next_sibling('value').string.replace(',', '.'))
        unit = value_2/nominal_2
        result = round(amount/unit ,4)
    else:
        nominal_2 = Decimal(soup.find("charcode", text=cur_to).find_next_sibling('nominal').string.replace(',', '.'))
        value_2 = Decimal(soup.find("charcode", text=cur_to).find_next_sibling('value').string.replace(',', '.'))
        unit_2 = value_2/nominal_2

        nominal_1 = Decimal(soup.find("charcode", text=cur_from).find_next_sibling('nominal').string.replace(',', '.'))
        value_1 = Decimal(soup.find("charcode", text=cur_from).find_next_sibling('value').string.replace(',', '.'))
        unit_1 = value_1/nominal_1

        result = round(amount*unit_1/unit_2 ,4)

    return result  # не забыть про округление до 4х знаков после запятой


if __name__ == '__main__':
    convert(1, "RUR", "USD", "10/04/2019", requests)
