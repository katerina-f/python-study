# -*- coding: utf-8 -*-

import vk
from classes.config import BaseConfig
import json
import time

class BaseUser:

    def __init__(self, user_id, token):
        version = '5.101'
        token = token
        self.user_id = user_id
        self.config = BaseConfig()
        self.fields = self.config.fields
        session = vk.Session(access_token=token)
        self.vk_api = vk.API(session, v=version, timeout=10)


class MainUser(BaseUser):

    def __init__(self, user_id, token):
        BaseUser.__init__(self, user_id, token)

    def get_user_data(self):
        data = self.vk_api.users.get(user_ids=self.user_id, fields=self.fields)[0]
        try:
            data['country'] = data['country']['id']
        except KeyError:
            pass

        try:
            data['city']  = data['city']['id']
        except KeyError:
            pass
        return data

    def get_data_for_search(self):
        data = self.get_user_data()

        for field in data:
            if data[field]:
                pass
            elif field == 'movies':
                data[field] = self.config.get_movie_for_search()
            elif field == 'books':
                data[field] = self.config.get_book_for_search()
            elif field == 'music':
                data[field] = self.config.get_music_for_search()
            elif field == 'interests':
                data[field] = self.config.get_interest_for_search()

        data['movies'] = data['movies'].split(",")
        data['books'] = data['books'].split(",")
        data['music'] = data['music'].split(",")
        data['interests'] = data['interests'].split(",")
        data['sex'] = self.config.get_sex_for_search()
        data['age_from'], data['age_to'] = self.config.get_age_for_search()

        return data


class MatchingUser(BaseUser):

    def __init__(self, user_id, token):
        BaseUser.__init__(self, user_id, token)

    def get_top_3_photos(self):
        owner_id = self.vk_api.users.get(user_ids=self.user_id, is_close=0, can_access_closed=1,fields=self.fields)[0]['id']
        try:
            raw_photos = self.vk_api.photos.get(count=10, album_id='profile',
                                    extended=1, owner_id=owner_id,)['items']
        except vk.exceptions.VkAPIError:
            raw_photos = []


        photos = []
        for photo in raw_photos:
            ph = {'id': photo['id'], 'likes': photo['likes']['count'],
                    'url': photo['sizes'][2]['url']}
            photos.append(ph)
        photos.sort(key=lambda x: x['likes'], reverse=True)

        return photos[:3]

    def write_to_json(self):
        photos = self.get_top_3_photos()
        result = {'user': self.user_id, 'photos': photos}
        try:
            with open('output_data/matching_users.json', 'a') as f:
                json.dump(result, f, indent=4)
        except FileIsNotFound:
            with open('output_data/matching_users.json', 'w') as f:
                json.dump(result, f, indent=4)
