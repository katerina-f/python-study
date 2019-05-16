from bs4 import BeautifulSoup
from collections import deque
import re
import os

# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start

    for file in files:
        with open(path+file, 'r') as f:
            files[file] = []
            res = link_re.findall(f.read())
            for name in res:
                if name in files and name not in files[file] and name != file:
                    files[file].append(name)

    search_queue = deque()
    search_queue += files[start]
    file_names = {start : None}

    while search_queue:
        parent = search_queue.popleft()
        for file in files[parent]:
            if file not in file_names:
                search_queue += files[parent]
                file_names[file] = parent

    return file_names

# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = [end]
    # TODO Добавить нужные страницы в bridge
    file = end
    while file is not start:
        file = files[file]
        if file is None:
            break
        else:
            bridge.append(file)

    return list(reversed(bridge))


def get_count_imgs(body):
    imgs = body.findAll('img')
    widths = []
    for img in imgs:
        try:
            img = int(img['width'])
            if img > 199:
                widths.append(img)
        except KeyError:
            pass
    return len(widths)


def get_count_headers(body):
    headers = body.find_all(re.compile('^h[1-6]$'))
    count = 0
    for header in headers:
        text = header.text
        if text.startswith('E') or text.startswith('C') or text.startswith('T'):
            count += 1

    return count


def get_links_len(body):
    linkslen = 0
    for a in body.find_all('a'):
        a_siblings = a.find_next_siblings()
        len_arr = 1
        for sib in a_siblings:
            if sib.name == 'a':
                len_arr+=1
            else:
                break
        if len_arr > linkslen:
            linkslen = len_arr

    return linkslen


def get_count_lists(body):
    lists = 0
    for ul in body.find_all('ul'):
        if ul.parent.name == 'div' or ul.parent.name == "td":
            lists += 1
    for ol in body.find_all('ol'):
        if ol.parent.name == 'div' or ul.parent.name == "td":
            lists += 1

    return lists

def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)
    # Искать список страниц можно как угодно, даже так: bridge = [end, start]
    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")
        body = soup.find(id="bodyContent")
        # TODO посчитать реальные значения

        imgs = get_count_imgs(body)  # Количество картинок (img) с шириной (width) не меньше 200
        headers = get_count_headers(body)  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = get_links_len(body)  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = get_count_lists(body)  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]
    return out
