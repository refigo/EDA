from setuptools import find_packages
from setuptools import setup

setup(
    name='yolo_inference',
    version='0.0.0',
    packages=find_packages(
        include=('yolo_inference', 'yolo_inference.*')),
)
