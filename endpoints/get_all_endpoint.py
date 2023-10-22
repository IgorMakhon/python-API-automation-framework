import requests
from endpoints.endpoints_handler import Endpoint


class GetAllPost(Endpoint):
    title = None
    body = None
    userId = None
    id = None

    def get_all_post(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        self.status = response.status_code
        self.title = response.json()['title']
        self.body = response.json()['body']
        self.userId = response.json()['userId']
        self.id = response.json()['id']
        return response

    def check_title(self):
        assert self.title is not None

    def check_body(self):
        assert self.body is not None

    def check_userId(self):
        assert self.userId is not None

    def check_id(self):
        assert self.id is not None
