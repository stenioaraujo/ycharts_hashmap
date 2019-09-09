from ycharts_hashmap import validations


class Hashmap:
    def __init__(self, array_size=100):
        """Create a Hashmap instance

        :param array_size: the underlying array size
        :raises: InvalidParameter when array_size is not greater than 0
        """
        validations.greater_than(array_size, 0)

        self._array = [None] * array_size

    @property
    def array_size(self):
        """Return the undelying array size"""
        return len(self._array)
