import pytest


@pytest.mark.put_endpoint
def test_put_status_ok(
        put_post_fixture, random_string_5_chars, random_string_10_chars, random_int, start_end_session
):
    # put the post with the rand_id
    put_post_fixture.put_post(random_string_5_chars, random_string_10_chars, random_int)
    put_post_fixture.check_status_is_ok()


@pytest.mark.put_endpoint
def test_put_id_is_int_type(put_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    # put the post with the rand_id
    put_post_fixture.put_post(random_string_5_chars, random_string_10_chars, random_int)
    put_post_fixture.check_id_is_int_type()


@pytest.mark.put_endpoint
def test_put_body_value_is_updated(put_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    updated_body = random_string_10_chars
    # put the post with the rand_id
    put_post_fixture.put_post(random_string_5_chars, random_string_10_chars, random_int)
    put_post_fixture.check_body_value_is_updated(updated_body)
