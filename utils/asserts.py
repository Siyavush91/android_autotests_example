from utils.logger import Logger, logger
def assert_equal(value1, value2):
    assert value1 == value2, f"{value1} is not equal {value2}"

def assert_true(value, error_message):
    assert value, error_message

def assert_false(value, error_message):
    assert not value, error_message

def assert_in(value, values):
    assert value in values, f"{value} is not in {values}"

def assert_is_not_none(value):
    assert value is not None

def soft_assert_equal(value1, value2):
    try:
        assert_equal(value1, value2)
    except AssertionError as e:
        logger.soft_assert_fail = True
        logger.logs_exception(str(e))

def soft_assert_in(value1, value2):
    try:
        assert_in(value1, value2)
    except AssertionError as e:
        logger.soft_assert_fail = True
        logger.logs_exception(str(e))

def soft_assert_false(value, error_message):
    try:
        assert_false(value, error_message)
    except AssertionError as e:
        logger.soft_assert_fail = True
        logger.logs_exception(str(e))

def soft_assert_true(value, error_message):
    try:
        assert_true(value, error_message)
    except AssertionError as e:
        logger.soft_assert_fail = True
        logger.logs_exception(str(e))

def soft_assert_is_not_none(value):
    try:
        assert value is not None
    except AssertionError as e:
        logger.soft_assert_fail = True
        logger.logs_exception(str(e))