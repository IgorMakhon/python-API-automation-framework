import pytest
import random
import string


@pytest.fixture()
def random_string():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10))
