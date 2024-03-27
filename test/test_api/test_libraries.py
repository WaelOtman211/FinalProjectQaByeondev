import unittest
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.libraries_logic import LibrariesLogic
from infra.headers import headers


class TestLibrariesLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.api_libraries = LibrariesLogic(self.my_api,self.browser.url)

    def test_add_libraries_to_favorite(self):
        libraries_ids = "124551,62465"
        print(self.api_libraries.add_library_to_favorite(headers,endpoints=libraries_ids))

if __name__ == '__main__':
    unittest.main()
