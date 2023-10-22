import random
import string
import pytest
from endpoints.post_endpoint import CreatePost


@pytest.fixture()
def random_string_5_chars():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(5))  # Generate random title or body


@pytest.fixture()
def random_string_10_chars():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10))  # Generate random title or body


@pytest.fixture()
def random_int():
    return random.randint(1, 100)


@pytest.fixture()
def create_post_fixture():
    return CreatePost()
