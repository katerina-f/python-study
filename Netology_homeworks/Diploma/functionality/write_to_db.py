# -*- coding: utf-8 -*-

import psycopg2

def create_db(con):
    cursor = con.cursor()
    try:
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS vkinder (
                        id serial PRIMARY KEY,
                        first_name varchar(50) NOT NULL,
                        last_name varchar(50) NOT NULL,
                        domain varchar(50) NOT NULL);""")
    except psycopg2.errors.DuplicateTable:
        pass
    con.commit()


def add_candidate(user, con):
    cursor = con.cursor()
    cursor.execute("""
       INSERT into vkinder (id, first_name, last_name, domain)
       values (%s, %s, %s, %s)
       returning id
       """, (user['id'], user['first_name'],
             user['last_name'], user['domain']))
    con.commit()
