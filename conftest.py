import random
import string
import pytest
from endpoints.get_all_endpoint import GetAllPost
from endpoints.post_endpoint import CreatePost
from endpoints.get_by_id_endpoint import GetIdPost
from endpoints.put_endpoint import PutPost
from endpoints.patch_endpoint import PatchPost
from endpoints.delete_endpoint import DeletePost
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


@pytest.fixture()
def put_post_fixture():
    return PutPost()


@pytest.fixture()
def patch_post_fixture():
    return PatchPost()


@pytest.fixture()
def delete_post_fixture():
    return DeletePost()


@pytest.fixture(scope='class')
def start_end_session():
    print(f"\n{Fore.YELLOW}Initiate testing for a new endpoint.{Fore.RESET}")
