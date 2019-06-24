import os
import sys
import unittest
from mock import patch
from app import *


class TestGettingInfo(unittest.TestCase):

    def setUp(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        directories = os.path.join(current_path, 'fixtures/directories.json')
        documents = os.path.join(current_path, 'fixtures/documents.json')
        with open(directories, 'r+') as f:
            self.directories = f.read()
        with open(documents, 'r+') as f:
            self.documents = f.read()

    @patch('builtins.input', side_effect = '11-2')
    @patch('app.check_document_existance')
    def test_getting_name(self, *args):
        check_document_existance.return_value = True
        self.assertEqual(get_doc_owner_name(), document['name'])


if __name__ == '__main__':
    suite_1 = unittest.TestLoader().loadTestsFromTestCase(TestGettingInfo)
    unittest.TextTestRunner(verbosity=2).run(suite_1)
