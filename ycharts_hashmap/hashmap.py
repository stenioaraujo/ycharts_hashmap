from ycharts_hashmap import validations


class Hashmap:
    """
    Implementation with a hashmap using collections.deque to threat collisions

    e.g:
    hmap = Hashmap()
    hmap.put("bom dia", "good morning")
    hmap.put("tudo bem?", "how are you?")

    print(hmap.get("tudo bem?")) # how are you?
    print(hmap.get("bom dia")) # good morning
    """

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

    def get(self, key, default=None):
        """Return the value associated with the key

        :param key: the key to be used to retrieve the value
        :param default: the default value to return if the key is not found
        :returns: the value associated with the key, or the default value
        """
        pass

    def put(self, key, value):
        """Set the value associated with the key

        If the key is already being used in the Hashmap,
        replace it with the new value. Otherwise, create a new entry for
        the new key.

        :param key: the key associated with the value
        :param value: the value associated with the key
        """
        pass

    def delete(self, key):
        """Delete the entry associated with the key

        :param key: the key to be deleted
        :raises: KeyError when the key is not found in the Hashmap
        """
        pass
