from setuptools import find_packages
from setuptools import setup

setup(
    name='playing_turtle_package_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('playing_turtle_package_msgs', 'playing_turtle_package_msgs.*')),
)
