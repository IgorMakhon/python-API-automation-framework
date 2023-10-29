import requests
from endpoints.endpoints_handler import Endpoint


class PutPost(Endpoint):
    title = None
    body = None
    userid = None

    def put_post(self, title_value, body_value, user_id):
        response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{user_id}',
                                headers={'Content-Type': 'application/json'},
                                json={'title': title_value, 'body': body_value, 'userId': user_id}
                                )
        self.status = response.status_code
        self.title = response.json()['title']
        self.body = response.json()['body']
        self.userid = response.json()['userId']
        self.id = response.json()['id']
        return response

    def check_body_value_is_updated(self, body_updated):
        print("\ncurrent body:", self.body)  # for debug
        print("expected body:", body_updated)  # for debug
        assert self.body == body_updated
