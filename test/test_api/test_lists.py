import unittest
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.list_logic import ListLogic
from infra.headers import headers


class TestListLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.api_list = ListLogic(self.my_api, self.browser.url)

    def tearDown(self):
        self.out
        self.browser.close()

    def test_add_new_list_Of_books(self):
        list_Name= "lovee"
        description = "loveeeeeeee"
        list_Visibility= "false"
        isInstitutionalUser= "false"

        expected_message = "Successfully created a list"
        
        self.assertEqual(expected_message,
                         self.api_list.add_list_of_books(headers, list_Name, description, list_Visibility,
                                                         isInstitutionalUser)[
                             'message'])

    def test_delete_list_Of_books(self):
        print(self.api_list.delete_list_of_books(headers,self.api_list.return_list_of_specific_name('lovee',headers)))



if __name__ == '__main__':
    unittest.main()
