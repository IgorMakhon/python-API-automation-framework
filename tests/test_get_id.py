import pytest


@pytest.mark.get_id_endpoint
def test_get_id_status_ok(get_id_post_fixture, start_end_session, random_int):
    get_id_post_fixture.get_id_post(random_int)  # get post with the random id from 1 to 100
    get_id_post_fixture.check_status_is_ok()


@pytest.mark.get_id_endpoint
def test_get_id_title_is_not_empty(get_id_post_fixture, random_int):
    get_id_post_fixture.get_id_post(random_int)  # get post with the random id from 1 to 100
    get_id_post_fixture.check_title_in_get_id()


@pytest.mark.get_id_endpoint
def test_get_id_and_id_is_int(get_id_post_fixture, random_int):
    get_id_post_fixture.get_id_post(random_int)  # get post with the random id from 1 to 100
    get_id_post_fixture.check_id_is_int_in_get_id()
