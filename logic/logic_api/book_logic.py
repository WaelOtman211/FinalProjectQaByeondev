class BookLogic:
    def __init__(self, api_object, baseurl):
        self.api = api_object
        self.base_url = baseurl

    def add_book_to_specific_list(self, headers, list_id, item_id, is_institutional_user):
        url = f'{self.base_url}api/lists/{list_id}?listId={list_id}&itemId={item_id}&isInstitutionalUser={is_institutional_user}'
        response = self.api.api_post_request(url, headers=headers)
        return response.json()

    def delete_book_from_war_list(self, headers, list_id, item_id, is_institutional_user):
        url = f'{self.base_url}api/lists/{list_id}?listId={list_id}&itemId={item_id}&isInstitutionalUser={is_institutional_user}'
        response = self.api.api_delete_request(url, headers=headers)
        return response.json()

    def add_note_to_specific_book(self, headers, list_id, item_id, note, is_institutional_user):
        url = f'{self.base_url}api/lists/{list_id}?itemId={item_id}&note={note}&isInstitutionalUser={is_institutional_user}'
        response = self.api.api_patch_request(url, headers=headers)
        return response.json()

    def add_list_of_books(self, headers, list_name, description, list_Visibility, is_institutional_user):
        url = f'{self.base_url}api/lists?listName={list_name}&description={description}&listVisibility={list_Visibility}&isInstitutionalUser={is_institutional_user}'
        response = self.api.api_post_request(url, headers=headers)
        return response.json()

    def get_books_data_from_specific_list(self,headers,list_id):
        url = f'{self.base_url}api/lists/{list_id}?listDetails=true&limit=25&offset=1&orderBy=created-dsc&isInstitutionalUser=false'
        response = self.api.api_get_request(url, headers=headers)
        return response.json()

    def get_book_id_due_to_list_name_and_book_name(self, headers,list_id,book_name):
        response = self.get_books_data_from_specific_list(headers,list_id)
        for entry in response['entries']:
            if entry['title'] == book_name:
                return entry['id']
        return "there is no book in this name "
