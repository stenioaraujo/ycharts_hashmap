import pytest

from ycharts_hashmap.hashmap import Hashmap


def test_suuccessful_creation():
    array_size = 100

    hashmap = Hashmap(array_size)
    assert hashmap.array_size == array_size

    hashmap = Hashmap()
    assert hashmap.array_size == array_size


def test_put_and_read_element():
    hashmap = Hashmap()

    keys = ["bom dia", "tudo bem?"]
    values = ["good morning", "how are you?"]

    for i, key in enumerate(keys):
        hashmap.put(key, values[i])

    for i, value in enumerate(values):
        assert hashmap.get(keys[i]) == value


def test_read_key_not_in_hashmap():
    hashmap = Hashmap()

    key = "I DON'T EXIST"
    default = "DEFAULT"

    assert hashmap.get(key) is None
    assert hashmap.get(key, default) == default


def test_update_existing_key():
    hashmap = Hashmap()

    key = 0
    value1, value2 = 1, 2

    hashmap.put(key, value1)
    assert hashmap.get(key) == value1

    hashmap.put(key, value2)
    assert hashmap.get(key) == value2


def test_key_hash_collision():
    hashmap = Hashmap(array_size=1)

    keys = [1, 2]
    values = [1, 2]

    for i, key in enumerate(keys):
        hashmap.put(key, values[i])

    for i, value in enumerate(values):
        assert hashmap.get(keys[i]) == value

    assert hashmap.array_size == 1


def test_delete_key():
    hashmap = Hashmap()

    key = 1
    value = 2

    hashmap.put(key, value)
    assert hashmap.get(key) == value

    hashmap.delete(key)
    assert hashmap.get(key) is None


def test_delete_key_not_exist():
    hashmap = Hashmap()

    key = "bright world"

    with pytest.raises(KeyError):
        hashmap.delete(key)

    hashmap.put(key, key)
    hashmap.delete(key)

    with pytest.raises(KeyError):
        hashmap.delete(key)


def test_pythonic_put_read():
    hashmap = Hashmap()

    key = (1, "key")
    value = (1, "value")

    hashmap[key] = value

    assert hashmap[key] == value


def test_pythonic_read_nonexistent_key():
    hashmap = Hashmap()

    key = "I DON'T EXIST"

    with pytest.raises(KeyError):
        hashmap[key]


def test_pythonic_delete():
    hashmap = Hashmap()

    key = 1
    value = 2

    hashmap[key] = value
    assert hashmap[key] == value

    del hashmap[key]
    with pytest.raises(KeyError):
        hashmap[key]


def test_pythonic_in_hashmap():
    hashmap = Hashmap()

    key = 1
    value = 2

    hashmap[key] = value
    assert key in hashmap

    assert "I DON'T EXIST" not in hashmap


def test_pythonic_iterate_over_keys():
    hashmap = Hashmap()

    keys = [1, 2]

    for i, key in enumerate(keys):
        hashmap[key] = "A VALUE"

    count_keys = 0
    for key in hashmap:
        assert key in keys
        count_keys += 1

    assert count_keys == len(keys)


def test_pythonic_number_keys():
    hashmap = Hashmap()

    keys = [1, 2, 3]

    assert len(hashmap) == 0

    for i, key in enumerate(keys):
        hashmap[key] = "A VALUE"

    assert len(hashmap) == len(keys)

    hashmap[keys[0]] = "ANOTHER VALUE"
    assert len(hashmap) == len(keys)

    del hashmap[keys[0]]
    assert len(hashmap) == (len(keys) - 1)
