import concurrent.futures
import unittest

from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.book_logic import BookLogic
from logic.logic_api.list_logic import ListLogic
from logic.logic_ui.signIn_page import SignInPage  # Renamed to reflect new focus
from infra.headers import headers

class End2EndTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.api_book = BookLogic(self.my_api, self.browser.url)
        self.api_list = ListLogic(self.my_api, self.browser.url)

    def tearDown(self):
        self.browser.close_browser()

    def test_add_book_to_specific_list_and_note_to_specific_book(self, browser=None):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        end_2_end = SignInPage(driver)

        self.api_book.add_book_to_specific_list(headers,self.api_list.return_list_of_specific_name('love',headers),"828890184","false")
        self.api_book.add_note_to_specific_book(headers,self.api_list.return_list_of_specific_name('love',headers),
                                                "828890184","i love read book","false")
        self.assertEqual('i love read book', end_2_end.sign_in_flow("wael.otman.97@gmail.com", "Wael@1234"))



    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_add_book_to_specific_list_and_note_to_specific_book, self.browser.browser_types)
        else:
            self.test_add_book_to_specific_list_and_note_to_specific_book(self.browser.default_browser)





