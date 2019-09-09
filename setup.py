import setuptools
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = [x.strip() for x in f.readlines()]

setuptools.setup(
    name='ycharts_hashmap',
    version='0.0.1',
    keywords='ycharts hashmap challenge',
    author='Stenio Araujo',
    author_email='stenio@hiaraujo.com',
    description=(
        'ycharts_hashmap is a module that contains the class Hashmap. '
        'It is a hashmap implementation for the ycharts challenge.'),
    long_description=long_description,
    url='https://github.com/stenioaraujo/ycharts_hashmap',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    entry_points={}
)
