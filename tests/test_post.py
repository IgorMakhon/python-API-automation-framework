def test_post_status_ok(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)
    create_post_fixture.check_status_is_ok()


def test_post_title_is_not_none(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)


def test_post_id_is_not_none(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)
    create_post_fixture.check_id()


def test_post_userid_is_not_none(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)
    create_post_fixture.check_userId()


def test_post_body_is_not_none(create_post_fixture, random_string_5_chars, random_string_10_chars, random_int):
    create_post_fixture.create_post(random_string_5_chars, random_string_10_chars, random_int)
    create_post_fixture.check_body()
