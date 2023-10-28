import pytest


@pytest.mark.get_all_endpoint
def test_get_all_status_ok(get_all_post_fixture, start_end_session):
    get_all_post_fixture.get_all_post()  # get all posts
    get_all_post_fixture.check_status_is_ok()  # test that the status in [200, 201]


@pytest.mark.get_all_endpoint
def test_get_all_title_is_not_empty(get_all_post_fixture):
    get_all_post_fixture.get_all_post()  # get all posts
    get_all_post_fixture.check_title_in_get_all()


@pytest.mark.get_all_endpoint
def test_get_all_id_is_int(get_all_post_fixture):
    get_all_post_fixture.get_all_post()  # get all posts
    get_all_post_fixture.check_id_is_int_in_get_all()
