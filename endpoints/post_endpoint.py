import requests
from endpoints.endpoints_handler import Endpoint


class CreatePost(Endpoint):
    title = None
    body = None
    userId = None
    id = None

    def create_post(self, title_value, body_value, user_id):
        response = requests.post('https://jsonplaceholder.typicode.com/posts',
                                 headers={'Content-Type': 'application/json'},
                                 json={'title': title_value, 'body': body_value, 'userId': user_id}
                                 )
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
