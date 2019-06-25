import app
import json
from mock import patch
import os
import unittest


class TestGettingInfo(unittest.TestCase):

    def setUp(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        f_directories = os.path.join(current_path, 'fixtures/directories.json')
        f_documents = os.path.join(current_path, 'fixtures/documents.json')
        with open(f_directories, 'r+') as f:
            self.dirs = json.load(f)
        with open(f_documents, 'r+') as f:
            self.docs = json.load(f)

    def tearDown(self):
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        f_directories = os.path.join(current_path, 'fixtures/directories.json')
        f_documents = os.path.join(current_path, 'fixtures/documents.json')
        with open(f_documents, 'r') as f:
            app.documents = json.load(f)
        with open(f_directories, 'r+') as f:
            app.directories = json.load(f)

    @patch('builtins.input', side_effect=['11-2'])
    def test_get_name_from_number(self, input):
        self.assertEqual(app.get_doc_owner_name(), 'Геннадий Покемонов')

    def test_get_names(self, *args):
        self.assertEqual(sorted(list(app.get_all_doc_owners_names())), sorted([doc['name'] for doc in self.docs]))

    def test_show_info(self):
        for doc in self.docs:
            info = '{} "{}" "{}"'.format(doc['type'], doc['number'], doc['name'])
            self.assertEqual(app.show_document_info(doc), info)

    def test_add_doc(self):
        app.append_doc_to_shelf('3365', '3')
        self.assertEqual(app.directories['3'][-1], '3365')

    @patch('builtins.input', side_effect=['11-2'])
    def test_del_doc(self, input):
        app.delete_doc()
        self.assertEqual(len(app.documents), 2)

    def test_remove_from_shelf(self):
        app.remove_doc_from_shelf('10006')
        self.assertFalse(app.directories['2'])


if __name__ == '__main__':
    suite_1 = unittest.TestLoader().loadTestsFromTestCase(TestGettingInfo)
    unittest.TextTestRunner(verbosity=2).run(suite_1)
