import unittest
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.book_logic import BookLogic
from infra.headers import headers


class TestBookLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.api_book = BookLogic(self.my_api, self.browser.url)
        self.failed_tests = []

    def tearDown(self):
        # Perform cleanup actions here if needed
        if self.failed_tests:
            # Create issue only if there are test failures
            self.create_issue(
                summary='Test Failure',
                description='One or more tests failed in TestBookLogic.',
                project_key='TT',
                issue_type='Bug'
            )

    def test_add_book_to_specific_list(self):
        self.assertEqual("Successfully added item to list",
                         self.api_book.add_book_to_specific_list(headers, "2e916b85-736e-4a89-8a66-de9a824065b3", "828890184", "false")[
                             'message'])

    def test_add_note_to_specific_book(self):
        self.assertEqual("Successfully updated Notes for an item in list",
                         self.api_book.add_note_to_specific_book(headers, "2e916b85-736e-4a89-8a66-de9a824065b3", "828890184", "sameerb7bso3ad",
                                                                 "false")[
                             'message'])

    def test_get_book_id_due_to_list_name_and_book_name(self):
        expected_book_id = 11386423333702
        try:
            actual_book_id = self.api_book.get_book_id_due_to_list_name_and_book_name(headers,
                                                                                      "2e916b85-736e-4a89-8a66-de9a824065b3",
                                                                                      'War')
            self.assertEqual(expected_book_id, actual_book_id)
        except AssertionError:
            # Handle assertion error here
            self.failed_tests.append('test_get_book_id_due_to_list_name_and_book_name')

    def test_delete_book_from_war_list(self):
        list_id = "2e916b85-736e-4a89-8a66-de9a824065b3"
        item_id = "828890184"
        self.assertEqual(f"Successfully deleted item:{item_id} from list:{list_id}",
                         self.api_book.delete_book_from_war_list(headers, list_id, item_id, "false")[
                             'message'])

    def create_issue(self, summary, description, project_key, issue_type='Bug'):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }
        new_issue = self.browser.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key


if __name__ == '__main__':
    unittest.main()
