import pytest

from ycharts_hashmap import exceptions
from ycharts_hashmap import validations


def test_greater_than_success():
    numbers = range(-4, 11)
    targets = range(-5, 10)

    for i in range(len(numbers)):
        validations.greater_than(numbers[i], targets[i])


def test_greater_than_failure():
    numbers = range(-5, 10)
    targets = range(-4, 11)

    for i in range(len(numbers)):
        with pytest.raises(exceptions.InvalidParameter):
            validations.greater_than(numbers[i], targets[i])
