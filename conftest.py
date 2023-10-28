import random
import string

import pytest

from endpoints.get_all_endpoint import GetAllPost
from endpoints.post_endpoint import CreatePost
from endpoints.get_by_id_endpoint import GetIdPost
from colorama import Fore


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


@pytest.fixture()
def get_all_post_fixture():
    return GetAllPost()


@pytest.fixture()
def get_id_post_fixture():
    return GetIdPost()


@pytest.fixture(scope='class')
def start_end_session():
    print(f"\n{Fore.YELLOW}Start tests for a new ENDPOINT{Fore.RESET}")
