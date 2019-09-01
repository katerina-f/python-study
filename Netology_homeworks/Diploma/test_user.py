import json
import os
import unittest
from mock import patch, Mock
from classes import config
from classes import vk_users


class TestUser(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        f_expect_user = os.path.join(current_path, 'fixtures/expect_user.json')
        f_raw_user = os.path.join(current_path, 'fixtures/raw_user.json')
        f_expect_user_for_config = os.path.join(current_path,
                                                'fixtures/expect_user_for_config.json')
        f_criteria = os.path.join(current_path, 'fixtures/criteria.json')
        with open(f_expect_user, "r") as f:
            self.expect_user = json.load(f)
        with open(f_raw_user, "r") as f:
            self.raw_user = json.load(f)
        with open(f_expect_user_for_config, "r") as f:
            self.expect_user_for_config = json.load(f)
        with open(f_criteria, "r") as f:
            self.criteria = json.load(f)

    @patch('classes.vk_users.BaseUser', autospec=True)
    def test_return_right_user_data(self, f):
        u = vk_users.MainUser(1, 2)
        u.data = self.raw_user
        result = u.get_user_data()
        self.assertEqual(result, self.expect_user)

    @patch('classes.vk_users.BaseUser', autospec=True)
    @patch('classes.config.BaseConfig', autospec=True)
    def test_return_full_data(self, f_1, f_2):
        mock = Mock()
        u = vk_users.MainUser(1, 2)
        u.data = self.expect_user
        u.fields = self.criteria
        mock.get_sex_for_search.return_value = 2
        mock.get_age_for_search.return_value = (28, 32)
        mock.get_music_for_search.return_value = ''
        mock.get_book_for_search.return_value = "Достоевский"
        mock.get_movie_for_search.return_value = "12 Angry Men"
        mock.get_interest_for_search.return_value = ''
        u.config = mock
        result = u.get_data_for_search()
        self.assertEqual(result, self.expect_user_for_config)

if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestUser)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
