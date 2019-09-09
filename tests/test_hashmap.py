from ycharts_hashmap.hashmap import Hashmap


def test_suuccessful_creation():
    array_size = 100

    hashmap = Hashmap(array_size)
    assert hashmap.array_size == array_size

    hashmap = Hashmap()
    assert hashmap.array_size == array_size
