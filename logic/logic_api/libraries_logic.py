class LibrariesLogic:
    def __init__(self, api_object, baseurl):
        self.api = api_object
        self.base_url = baseurl

    def add_library_to_favorite(self, headers, endpoints):
        url = f'{self.base_url}api/user-profile/search-relevancy?searchRelevancy={endpoints}'
        response = self.api.api_patch_request(url, headers=headers)
        return response

