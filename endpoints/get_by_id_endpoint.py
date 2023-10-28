import requests
from endpoints.endpoints_handler import Endpoint


class GetIdPost(Endpoint):
    title = None
    body = None
    userid = None
    id = None

    def get_id_post(self, id_rand):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id_rand}')
        self.status = response.status_code
        self.title = response.json()['title']
        self.body = response.json()['body']
        self.userid = response.json()['userId']
        self.id = response.json()['id']
        return response

    def check_title_in_get_id(self):
        print("\ntitle:", self.title)
        assert self.title is not None

    def check_body_in_get_id(self):
        print("\nbody:", self.body)
        assert self.body is not None

    def check_userid_in_get_id(self):
        print("\nuserid:", self.userid)
        assert self.userid is not None

    def check_id_is_int_in_get_id(self):
        print("\nid:", self.id)
        assert isinstance(self.id, int)