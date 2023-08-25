from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'yolo_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob(os.path.join('launch','*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ksh',
    maintainer_email='ksh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'image_publisher = yolo_pkg.img_pub:main',
        'object_detect_publisher = yolo_pkg.object_detection_pub:main',
        'object_detect_subscriber = yolo_pkg.object_detection_sub:main',
        'dobot_executor = yolo_pkg.dobot_executor:main'
        ],
    },
)
