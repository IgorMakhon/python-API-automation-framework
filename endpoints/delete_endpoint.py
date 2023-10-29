import requests
from endpoints.endpoints_handler import Endpoint


class DeletePost(Endpoint):
    body = None

    def delete_post(self, user_id):
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{user_id}')
        self.status = response.status_code
        self.body = response.json()
        return response

    def check_body_is_empty_brackets(self):
        print("\ncurrent body:", self.body)  # for debug
        assert self.body == {}
