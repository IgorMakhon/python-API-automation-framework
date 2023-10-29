import requests
from endpoints.endpoints_handler import Endpoint


class PatchPost(Endpoint):
    title = None

    def patch_post(self, title_value, user_id):
        response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{user_id}',
                                  headers={'Content-Type': 'application/json'},
                                  json={'title': title_value}
                                  )
        self.status = response.status_code
        self.title = response.json()['title']
        self.id = response.json()['id']
        return response

    def check_title_value_is_updated(self, title_updated):
        print("\ncurrent title:", self.title)  # for debug
        print("expected title:", title_updated)  # for debug
        assert self.title == title_updated
