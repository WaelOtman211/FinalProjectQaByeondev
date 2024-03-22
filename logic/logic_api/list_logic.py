class ListLogic:

    def __init__(self, api_object, baseurl):
        self.api = api_object
        self.base_url = baseurl

    def add_list_of_books(self, headers, list_name, description, list_Visibility, is_institutional_user):
        url = f'{self.base_url}api/lists?listName={list_name}&description={description}&listVisibility={list_Visibility}&isInstitutionalUser={is_institutional_user}'
        response = self.api.api_post_request(url, headers=headers)
        return response.json()

    def get_all_list_data(self, headers):
        url = f'{self.base_url}api/lists?limit=10&offset=1&orderBy=name-asc&isInstitutionalUser=false&listName ='
        response = self.api.api_get_request(url, headers=headers)
        return response.json()

    def return_list_of_specific_name(self,name, headers):
        url = f'{self.base_url}api/lists?limit=10&offset=1&orderBy=name-asc&isInstitutionalUser=false&listName ='
        response = self.api.api_get_request(url, headers=headers)
        for entry in response.json()['listsData']['entries']:
            if entry['listName'] == name:
                return entry['id']

        return "there is no list in that name "
