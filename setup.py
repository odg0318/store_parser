from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Store parser',
    version='0.1.0',
    description='A parser for googleplay and appstore',
    long_description=readme,
    author='guri',
    author_email='odg0318@gmail.com',
    url='https://github.com/odg0318/store_parser',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

