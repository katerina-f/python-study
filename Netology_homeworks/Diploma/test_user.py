from classes.vk_users import MainUser, MatchingUser
import unittest

class TestUser(unittest.TestCase):

    def setUp(self):
        token = input('Введите токен')
        self.obj = MainUser('1', token)
        self.obj_2 = MatchingUser('1', token)


    def test_return_right_user_data(self):
        data = {'id': 1, 'first_name': 'Павел', 'last_name': 'Дуров', 'is_closed': False, 'can_access_closed': True, 'sex': 2, 'domain': 'durov', 'city': 2, 'country': 1, 'common_count': 0, 'interests': '', 'music': '', 'movies': '12 Angry Men', 'books': ''}
        result = self.obj.get_user_data()
        self.assertEqual(result, data)


    def test_return_right_photos(self):
        data = [{'id': 288668576, 'likes': 1459882, 'url': 'https://pp.userapi.com/c7003/v7003978/1edb/S9N9m1NFFx4.jpg'}, {'id': 263219656, 'likes': 972081, 'url': 'https://pp.userapi.com/c9591/u00001/136592355/x_dbfafe4c.jpg'}, {'id': 263219735, 'likes': 868439, 'url': 'https://pp.userapi.com/c9591/u00001/136592355/x_d51dbfac.jpg'}]
        result = self.obj_2.get_top_3_photos()
        self.assertEqual(len(result), len(data))


if __name__ == '__main__':
    suite_1 = unittest.TestLoader().loadTestsFromTestCase(TestUser)
    unittest.TextTestRunner(verbosity=2).run(suite_1)
