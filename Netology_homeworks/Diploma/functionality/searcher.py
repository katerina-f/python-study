# -*- coding: utf-8 -*-
import time
from classes.vk_users import MainUser
from functionality.write_to_db import add_candidate
import psycopg2


def search(user, data, count):
    fields = user.fields

    code = '''
    var i = 0;
    var users = [];
    var offset = %d + 1000;
    while (i < 2){
    users = users + API.users.search({"city": %s, "sex": %d, "age_from": %d, "age_to": %d, "fields": "%s", "count": 1000}).items;
    i = i + 1;
    offset = offset + 1000;}
    return users;
    ''' % (count, data['city'], data['sex'], data['age_from'], data['age_to'], fields)

    result = user.vk_api.execute(code=code)
    return result


def search_matching_users(con, user_id, token):
    cursor = con.cursor()
    user = MainUser(user_id, token)
    data = user.get_data_for_search()

    cursor.execute('''SELECT id FROM vkinder''')
    start = [i[0] for i in cursor.fetchall()]
    users = []
    count = len(start)

    result = search(user, data, count)

    for u in result:
        try:
            add_candidate(u, con)
            users.append(u)
        except psycopg2.errors.UniqueViolation:
            pass

    print(f'Найдено еще {len(users)} пользователей по вашему запросу')
    print('Если хотите поискать еще, запустите программу снова!')
    return users, data
