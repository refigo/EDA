from setuptools import setup

package_name = 'playing_turtle_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'total_subscriber = playing_turtle_package.total_subscriber:main',
            'tree_spawning_server = playing_turtle_package.tree_spawning_service_server:main'
        ],
    },
)
