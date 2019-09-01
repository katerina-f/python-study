# -*- coding: utf-8 -*-
import json
import vk
from classes.config import BaseConfig


class BaseUser:
    def __init__(self, user_id, token):
        version = '5.101'
        token = token
        self.user_id = user_id
        self.config = BaseConfig()
        self.fields = self.config.fields
        session = vk.Session(access_token=token)
        self.vk_api = vk.API(session, v=version, timeout=10)
        self.data = self.vk_api.users.get(user_ids=self.user_id, fields=self.fields)[0]


class MainUser(BaseUser):
    def __init__(self, user_id, token):
        BaseUser.__init__(self, user_id, token)

    def get_user_data(self):
        try:
            self.data['country'] = self.data['country']['id']
        except KeyError:
            pass

        try:
            self.data['city'] = self.data['city']['id']
        except KeyError:
            pass
        return self.data

    def get_data_for_search(self):
        for field in self.fields:
            try:
                self.data[field]
            except KeyError:
                if field == 'movies':
                    self.data[field] = self.config.get_movie_for_search()
                if field == 'books':
                    self.data[field] = self.config.get_book_for_search()
                if field == 'music':
                    self.data[field] = self.config.get_music_for_search()
                if field == 'interests':
                    self.data[field] = self.config.get_interest_for_search()

        self.data['movies'] = self.data['movies'].split(",")
        self.data['books'] = self.data['books'].split(",")
        self.data['music'] = self.data['music'].split(",")
        self.data['interests'] = self.data['interests'].split(",")
        self.data['sex'] = self.config.get_sex_for_search()
        self.data['age_from'], self.data['age_to'] = self.config.get_age_for_search()

        return self.data


class MatchingUser(BaseUser):

    def __init__(self, user_id, token):
        BaseUser.__init__(self, user_id, token)

    def get_top_3_photos(self):
        owner_id = self.vk_api.users.get(user_ids=self.user_id,
                                         is_close=0, can_access_closed=1,
                                         fields=self.fields)[0]['id']
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
        except FileNotFoundError:
            with open('output_data/matching_users.json', 'w') as f:
                json.dump(result, f, indent=4)
