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
        self._num_keys = 0

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
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __getitem__(self, key):
        """Return the value associated with the key

        :param key: the key to be used to retrieve the value
        :returns: the value associated with the key, or the default value
        :raises: KeyError when the key is not found in the Hashmap
        """
        key_hash = self._hash(key)

        index_key = self._index_of_key(key_hash, key)
        if index_key != -1:
            pair = self._array[key_hash][index_key]
            return pair[1]

        raise KeyError(key)

    def put(self, key, value):
        """Set the value associated with the key

        If the key is already being used in the Hashmap,
        replace it with the new value. Otherwise, create a new entry for
        the new key.

        :param key: the key associated with the value
        :param value: the value associated with the key
        :raises: TypeError if key is unhashable
        """
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        key_hash = self._hash(key)

        index_key = self._index_of_key(key_hash, key)
        if index_key == -1:
            if self._array[key_hash]:
                self._array[key_hash].append([key, value])
            else:
                self._array[key_hash] = [[key, value]]
            self._num_keys += 1
        else:
            pair = self._array[key_hash][index_key]
            pair[1] = value

    def _hash(self, key):
        """Hash the key taking in account the underlying array size

        Hash the key to a number that can be mapped to an index
        on the underlaying array.

        :param key: the key to be hashed
        :returns: the number representing the hash
        :raises: TypeError if the is unhashable
        """
        key_hash = hash(key)

        return key_hash % self.array_size

    def _index_of_key(self, key_hash, key):
        """Find the index of a key in the underlying array at key_hash

        :param key_hash: the position in the underlying array to search on
        :param key: the key to be found
        :returns: the index if the key is found, -1 otherwise
        """
        pairs = self._array[key_hash]
        if pairs:
            for i, pair in enumerate(pairs):
                if pair[0] == key:
                    return i

        return -1

    def delete(self, key):
        """Delete the entry associated with the key

        :param key: the key to be deleted
        :raises: KeyError when the key is not found in the Hashmap
        """
        self.__delitem__(key)

    def __delitem__(self, key):
        key_hash = self._hash(key)

        index_key = self._index_of_key(key_hash, key)
        if index_key == -1:
            raise KeyError(key)
        else:
            del self._array[key_hash][index_key]
            self._num_keys -= 1

    def __contains__(self, key):
        """Verify if key is in the Hashmap

        :param key: the key to be checked
        :returns: True if the key is in the Hashmap, False otherwise
        """
        key_hash = self._hash(key)

        index_key = self._index_of_key(key_hash, key)
        return index_key != -1

    def __iter__(self):
        """Iterate over all the keys in the Hashmap

        :returns: A generator for all the keys in the Hashmap
        """
        for arr_pos in self._array:
            if arr_pos:
                for key, value in arr_pos:
                    yield key

    def __len__(self):
        """Return the number of keys in the Hashmap

        :returns: the number of keys in the Hashmap
        """
        return self._num_keys
