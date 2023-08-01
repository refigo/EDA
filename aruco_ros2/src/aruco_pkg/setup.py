from setuptools import setup

from glob import glob
import os

package_name = 'aruco_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/params', glob(os.path.join('params', '*.npz'))),
        ('share/' + package_name + '/params', glob(os.path.join('params', '*.yaml'))),
        ('share/' + package_name + '/launch', glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gomi',
    maintainer_email='42.4.mgo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_publisher = aruco_pkg.img_pub:main',
            'marker_4X4_recognition = aruco_pkg.aruco_4_recognition_node:main',
            'marker_5X5_recognition = aruco_pkg.aruco_5_recognition_node:main',
            'marker_6X6_recognition = aruco_pkg.aruco_6_recognition_node:main',
            'marker_7X7_recognition = aruco_pkg.aruco_7_recognition_node:main',
            'transform_broadcaster = aruco_pkg.tf_broadcast_node:main',
        ],
    },
)
