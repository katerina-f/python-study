import json
import os
import unittest
from functionality import saver


class TestFiltering(unittest.TestCase):

    def setUp(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        f_expect_user = os.path.join(current_path, 'fixtures/expect_user.json')
        f_criteria = os.path.join(current_path, 'fixtures/criteria.json')
        f_users_data = os.path.join(current_path, 'fixtures/users_data.json')
        with open(f_expect_user, "r") as f:
            self.expect_user = json.load(f)
        with open(f_criteria, "r") as f:
            self.criteria = json.load(f)
        with open(f_users_data, "r") as f:
            users_data = json.load(f)
            self.filtered_data = users_data["filtered_data"]
            self.raw_data = users_data["raw_data"]

    def test_return_right_score(self):
        result = saver.get_score_for_user(self.expect_user, self.criteria)
        self.assertEqual(result, 103)

    def test_filtering_users(self):
        result = saver.filter_for_users(self.raw_data, self.criteria)
        self.assertEqual(result, self.filtered_data)


if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestFiltering)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
