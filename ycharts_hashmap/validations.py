from ycharts_hashmap import exceptions


def greater_than(number, target):
    if number <= target:
        error_message = "{} is not greater than {}".format(number, target)
        raise exceptions.InvalidParameter(error_message)
