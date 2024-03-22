import unittest
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.book_logic import BookLogic
from infra.headers import headers


class TestPetLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.api_book = BookLogic(self.my_api, self.browser.url)

    def test_add_book_to_war_list(self):
        list_id = "2e916b85-736e-4a89-8a66-de9a824065b3"
        item_id = "828890184"
        is_institutional_user = "false"

        expected_message = "Successfully added item to list"
        self.assertEqual(expected_message,
                         self.api_book.add_book_to_war_list(headers, list_id, item_id, is_institutional_user)[
                             'message'])

    def test_add_note_to_specific_book(self):
        list_id = "2e916b85-736e-4a89-8a66-de9a824065b3"
        item_id = "828890184"
        note = "sameerb7bso3ad"
        isInstitutionalUser = "false"

        expected_message = f"Successfully updated Notes for an item in list"
        self.assertEqual(expected_message,
                         self.api_book.add_note_to_specific_book(headers, list_id, item_id, note,
                                                                 isInstitutionalUser)[
                             'message'])

    def test_get_book_id_due_to_list_name_and_book_name(self):
        list_id = "2e916b85-736e-4a89-8a66-de9a824065b3"
        book_name='War'

        expected_id = '1142371458'
        self.assertEqual(expected_id,self.api_book.get_book_id_due_to_list_name_and_book_name(headers,list_id,book_name))

    def test_delete_book_from_war_list(self):
        list_id = "2e916b85-736e-4a89-8a66-de9a824065b3"
        item_id = "828890184"
        is_institutional_user = "false"
        expected_message = f"Successfully deleted item:{item_id} from list:{list_id}"

        self.assertEqual(expected_message,
                         self.api_book.delete_book_from_war_list(headers, list_id, item_id, is_institutional_user)[
                             'message'])

if __name__ == '__main__':
    unittest.main()


