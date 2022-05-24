import unittest
from docs import check_document_existance, get_doc_owner_name, add_new_shelf, get_all_doc_owners_names, \
    delete_doc
from unittest.mock import patch


class TestDocuments(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance('11-2'), True, 'Should be True')

    @patch('docs.user_doc', return_value='2207 876234')
    def test_get_doc_owner_name(self, input):
        self.assertEqual(get_doc_owner_name(), 'Василий Гупкин', 'Should be "Василий Гупкин"')

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf(4), (4, True))

    @patch('docs.user_doc', return_value='11-2')
    def test_delete_doc(self, input):
        self.assertEqual(delete_doc(), ('11-2', True))

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Аристарх Павлов'})
