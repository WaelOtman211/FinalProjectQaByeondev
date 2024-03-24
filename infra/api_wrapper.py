import requests


class APIWrapper:

    def __init__(self):
        self.response = None

    def api_get_request(self, url, headers):
        self.response = requests.get(url, headers=headers)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self, url, headers, data=None):
        self.response = requests.post(url, headers=headers, json=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_patch_request(self, url, headers, data=None):
        self.response = requests.patch(url, headers=headers, json=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_delete_request(self, url, headers):
        self.response = requests.delete(url, headers=headers)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
