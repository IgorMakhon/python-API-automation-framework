import requests
from endpoints.endpoints_handler import Endpoint


class GetAllPost(Endpoint):
    title = None
    body = None
    userid = None

    def get_all_post(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        self.status = response.status_code
        self.title = response.json()[0]['title']
        self.body = response.json()[0]['body']
        self.userid = response.json()[0]['userId']
        self.id = response.json()[0]['id']
        return response

    def check_title_in_get_all(self):
        print("\ntitle:", self.title)
        assert self.title is not None

    def check_body_in_get_all(self):
        print("\nbody:", self.body)
        assert self.body is not None

    def check_userid_in_get_all(self):
        print("\nuserid:", self.userid)
        assert self.userid is not None
