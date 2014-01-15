from setuptools import setup, find_packages

import bento


setup(
    name='django-bento',
    version=bento.__version__,
    description=bento.__doc__,
    packages=find_packages(),
    url='http://github.com/lazybird/django-bento/',
    author='lazybird',
    long_description=open('README.md').read(),
    include_package_data=True,
    license='Creative Commons Attribution 3.0 Unported',
)

