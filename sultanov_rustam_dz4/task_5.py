import sys
import xml.etree.ElementTree as ET
import urllib.request
from decimal import Decimal


def currency_rates(currency):
    tree = ET.parse(urllib.request.urlopen('http://www.cbr.ru/scripts/XML_daily.asp'))
    root = tree.getroot()

    list_charcode = []
    list_value = []

    for elem in root:
        list_charcode.append(elem[1].text.lower())

    for elem in root:
        list_value.append(elem[4].text)

    dict_total = dict(zip(list_charcode, list_value))
    p = dict_total.setdefault(currency, '0')
    p = p.replace(',','.')
    p = Decimal(p)
    if p != 0:
        print(f'Текущий курс: {p.quantize(Decimal("1.0000"))} руб')
    else:
        print('!!!Нет такой валюты!!!')


# currency = input('Ведите валюту: ')
currency_rates(sys.argv[1])
