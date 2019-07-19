# -*- coding: utf-8 -*-
import psycopg2 as pg
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from functionality.write_to_db import create_db
from functionality.searcher import search_matching_users
from functionality.saver import save_matching_users


def main():
    con = pg.connect('host=localhost port=5432 dbname=vkinder user=vkinder')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    create_db(con)

    print('Добро пожаловать в VKinder - приложение для поиска пары!')
    user_id = input('Введите id пользователя для поиска: ')
    token = input('Введите токен для доступа: ')

    data, criteria = search_matching_users(con, user_id, token)
    save_matching_users(data, criteria, token)
    con.close()



if __name__ == '__main__':
    main()
