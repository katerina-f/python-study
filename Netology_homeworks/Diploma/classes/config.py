# -*- coding: utf-8 -*-

class BaseConfig:

    def __init__(self):
        self.fields = 'sex, city, country, common_count, \
        interests, music, movies, books, domain'

    def get_sex_for_search(self):
        while True:
            try:
                sex = int(input("Кого будем искать? \
                            Выберите пол: 1 - женский, \
                            2 - мужской, 0 - ищем оба"))
            except ValueError:
                print('Кажется вы использовали буквы! ')
                continue

            if int(sex) not in [0, 1, 2]:
                print('Вы выбрали неверную цифру! Пожалуйста, повторите!')
            else:
                return sex

    def get_age_for_search(self):
        while True:
            try:
                age_min = int(input('Введите минимальный возраст для поиска: '))
                age_max = int(input('Введите максимальный возраст для поиска: '))
            except ValueError:
                print('Кажется вы использовали буквы! ')
                continue

            if age_max <= age_min:
                print('Максимальный возраст не может быть меньше минимального, \
                        повторяем попытку!')
            elif any((age_max < 0, age_min < 0)):
                print('Возраст не может быть меньше 0!')
            else:
                return age_min, age_max

    def get_city_for_search(self):
        city = input('Введите город, где сейчас проживаете: ')
        return city

    def get_movie_for_search(self):
        movie = input('Введите свой любимый фильм: ')
        return movie

    def get_music_for_search(self):
        music = input('Введите своего любимого музыкального исполнителя/группу: ')
        return music

    def get_book_for_search(self):
        book = input('Введите свою любимую книгу(название или фамилию автора): ')
        return book

    def get_interest_for_search(self):
        interest = input('Введите свой наибольший интерес \
         (танцы, рисование, пение, спорт и т.д.): ')
        return interest
