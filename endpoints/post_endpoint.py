import requests
from endpoints.endpoints_handler import Endpoint


class CreatePost(Endpoint):
    title = None
    body = None
    userid = None

    def create_post(self, title_value, body_value, user_id):
        response = requests.post('https://jsonplaceholder.typicode.com/posts',
                                 headers={'Content-Type': 'application/json'},
                                 json={'title': title_value, 'body': body_value, 'userId': user_id}
                                 )
        self.status = response.status_code
        self.title = response.json()['title']
        self.body = response.json()['body']
        self.userid = response.json()['userId']
        self.id = response.json()['id']
        return response

    def check_title_not_none(self):
        print("\ntitle:", self.title)  # for debug
        assert self.title is not None

    def check_body_not_none(self):
        print("\nbody:", self.body)  # for debug
        assert self.body is not None

    def check_userid_not_none(self):
        print("\nuserid:", self.userid)  # for debug
        assert self.userid is not None
