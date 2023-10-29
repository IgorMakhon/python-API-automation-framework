import pytest


@pytest.mark.delete_endpoint
def test_delete_status_ok(delete_post_fixture, random_int, start_end_session):
    delete_post_fixture.delete_post(random_int)  # delete the post with the rand_id
    delete_post_fixture.check_status_is_ok()


@pytest.mark.delete_endpoint
def test_delete_is_empty_brackets(delete_post_fixture, random_int):
    delete_post_fixture.delete_post(random_int)  # delete the post with the rand_id
    delete_post_fixture.check_body_is_empty_brackets()
