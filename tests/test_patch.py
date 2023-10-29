import pytest


@pytest.mark.patch_endpoint
def test_patch_status_ok(patch_post_fixture, random_string_5_chars, random_int, start_end_session):
    patch_post_fixture.patch_post(random_string_5_chars, random_int)  # patch the title of the  post with the rand_id
    patch_post_fixture.check_status_is_ok()


@pytest.mark.patch_endpoint
def test_patch_id_is_int_type(patch_post_fixture, random_string_5_chars, random_int):
    patch_post_fixture.patch_post(random_string_5_chars, random_int)  # patch the title of the  post with the rand_id
    patch_post_fixture.check_id_is_int_type()


@pytest.mark.patch_endpoint
def test_patch_title_value_is_updated(patch_post_fixture, random_string_5_chars, random_int):
    updated_title = random_string_5_chars
    # patch the title of the  post with the rand_id
    patch_post_fixture.patch_post(random_string_5_chars, random_int)
    patch_post_fixture.check_title_value_is_updated(updated_title)
