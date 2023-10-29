import pytest


@pytest.mark.post_endpoint
def test_get_all_status_ok(
        create_post_fixture, random_string_5_chars, random_string_10_chars, random_int, start_end_session
):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)  # create a post
    create_post_fixture.check_status_is_ok()  # test that the status in [200, 201]


@pytest.mark.post_endpoint
def test_post_title_is_not_none(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)
    create_post_fixture.check_title_not_none()


@pytest.mark.post_endpoint
def test_post_id_is_int_type(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)
    create_post_fixture.check_id_is_int_type()


@pytest.mark.post_endpoint
def test_post_userid_is_not_none(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)
    create_post_fixture.check_userid_not_none()


@pytest.mark.post_endpoint
def test_post_body_is_not_none(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)
    create_post_fixture.check_body_not_none()
