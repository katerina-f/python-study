import csv
from datetime import datetime
from pprint import pprint
from pymongo import MongoClient
import re


def main():
    client = MongoClient()
    client.drop_database('playbill_db')
    playbill_db = client.playbill_db

    read_data('artists.csv', playbill_db)

    pprint(find_cheapest(playbill_db))
    pprint(find_by_name('Th', playbill_db))
    pprint(find_by_name('j', playbill_db))
    pprint(sort_by_date(7, playbill_db))


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    events = []
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        for event in reader:
            day, month, year = (event['Дата'] + '.2019').split('.')
            event['Дата'] = datetime(year=int(year), month=int(month), day=int(day))
            event['Цена'] = int(event['Цена'])
            events.append(dict(event))

    concert = db.concert
    result = concert.insert_many(events)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастания цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    sorted_events = [event for event in db.concert.find().sort('Цена')]
    return sorted_events


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """
    regex = re.compile(f'\w*{name}[\-\:\`]?\w*', re.IGNORECASE)
    artists = [artist for artist in db.concert.find({'Исполнитель' : regex}).sort('Цена')]
    return artists


def sort_by_date(month, db):
    """
    Отсортировать билеты из базы по дате
    """
    sorted_by_date = [event for event in db.concert.find().sort('Дата') if event['Дата'].month == month]
    return sorted_by_date


if __name__ == '__main__':
    main()
