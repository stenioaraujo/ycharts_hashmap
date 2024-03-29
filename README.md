# YCHARTS Challenge 1 - Hashmap

<p align="center">
<a href="https://travis-ci.com/stenioaraujo/ycharts_hashmap"><img src="https://img.shields.io/travis/com/stenioaraujo/ycharts_hashmap/master.svg?style=popout-square&label=Travis%20CI&logo=travis&logoColor=white" alt="Build Status" /></a>
<a href="https://github.com/stenioaraujo/ycharts_hashmap"><img src="https://img.shields.io/badge/Python-3.6%7C3.7-informational.svg?logo=python&style=popout-square" alt="Tested on Python 3.6, 3.7" /></a>
</p>

<p align="center">
<b>ycharts_hashmap</b> is a module that contains the class Hashmap. The ease of hashmaps.
</p>

## Overview

- Architectural decisions:
  - [x] Use list to threat collisions
    - By using list I can index a specific position and make the code less repetitive. The trade off is, delete operations will take O(n), where n is the number of keys with the same hash.
  - [x] Use python's hashing function
  - Define basic methods:
    - [x] get(key[, default])
    - [x] put(key, value)
    - [x] delete(key)
    - [x] \_\_getitem\_\_(key)
    - [x] \_\_setitem\_\_(key, value)
    - [x] \_\_delitem\_\_(key)
    - [x] \_\_contains\_\_(key)
    - [x] \_\_iter\_\_()
    - [x] \_\_len\_\_()
	- [x] \_\_reversed\_\_()
		- This was implemented to allow the iterator to be reversed
  - [x] Initially have a fixed size for the underlying array, the size can be passed as parameter on the constructor
  - [x] Make it a library that can be imported by other python programs
  - [x] Use pytest, pytest-cov and tox for testing
  - [x] Use travis as CI
  - [x] Make the underlying array grow when the number of keys reach the array\_size * resize\_multiplier
    - Each key is re-inserted in the Hashmap to allow rehashing.
    - By resizing and redistributing, we have a chance to lower the number of collisions.

## Requirements

This library was tested on Ubuntu 18.04, the following was used:

- [python 3.6](https://www.python.org/downloads/release/python-360/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [pipenv](https://docs.pipenv.org/en/latest/install/#installing-pipenv)

One can install the requirements with the following script:

``` bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip
pip3 install pipenv
```

## Testing

``` bash
git clone https://github.com/stenioaraujo/ycharts_hashmap
cd ycharts_hashmap
pipenv install --dev
pipenv run tox
```

## Install locally

``` bash
git clone https://github.com/stenioaraujo/ycharts_hashmap
cd ycharts_hashmap
pipenv run pip install .
pipenv shell
python # to start the interpreter
```

Any python application inside this virtual evnrionoment will have access to the `ychart_hashmap` library.

## Install Globally

``` bash
git clone https://github.com/stenioaraujo/ycharts_hashmap
cd ycharts_hashmap
pip3 install .
python3 # to start the interpreter
```

Other python applications on the system will have access to the `ychart_hashmap` library.

## Usage

The `Hashmap` class can be accessed through the `ycharts_hashmap` library, bellow it is shown how to use the features available.

Those commands can be ran directly on the python interpreter started on the preivous sections.

``` python
from ycharts_hashmap.hashmap import Hashmap

h = Hashmap() # initializes the Hashmap with 100 spots on the underlying array, the size is fixed

# Put new elements in the hashmap
h.put("one", 1)
h["two"] = 2
h["three"] = 3

# Get element using the key
print(h.get("two")) # 2
print(h["one"]) # 1

print(h["four"]) # KeyError, the key "four" is not in the Hashmap yet
print(h.get("four")) # it prints None, the default value of `.get` is `None`

# Delete a key
h.delete("two")
print(h.get("two", False)) # False

del h["one"]
print(h.get("one", False)) # False

h.delete("one") # KeyError, the key "one" is not in the Hashmap anymore
del h["two"] # Also KeyError

# in Statement
print("one" in h) # False, there is no key "one" in the Hashmap

h["one"] = 1
print("one" in h) # True

# Iterate over the keys
for key in h:
    print(key) # Will print "one" and "three"

# Iterate over the keys in reverse order
for key in reversed(h):
    print(key)

# Iterate over the keys and values
for key, value in h.items():
    print(key, value) # "one 1" and "three 3"

# Get the number of keys in the Hashmap
print(len(h)) # 2
```

For more information:

``` python
from ycharts_hashmap.hashmap import Hashmap

help(Hashmap)
```
