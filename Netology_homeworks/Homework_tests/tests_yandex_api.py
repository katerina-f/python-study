from api import API
import requests
import unittest


URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class TestTranslaterApi(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    def test_get_response_200(self):
        params = {'key': API, 'lang': 'ru', 'text': 'hello'}
        response = self.session.get(URL, params=params)
        print(response.json()['text'][0])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['text'][0], 'привет')

    def test_get_response_401(self):
        params = {'key': '0', 'lang': 'en'}
        response = self.session.get(URL, params=params)
        print(response.json()['message'])
        self.assertEqual(response.json()['code'], 401)

    def test_get_response_502(self):
        params = {'key': API, 'lang': 'iwpqpqp'}
        response = self.session.get(URL, params=params)
        print(response.json()['message'])
        self.assertEqual(response.json()['code'], 502)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTranslaterApi)
    unittest.TextTestRunner(verbosity=2).run(suite)
