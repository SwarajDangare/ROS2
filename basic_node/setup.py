from setuptools import find_packages, setup

package_name = 'basic_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='swaraj',
    maintainer_email='swaraj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "oop_node = basic_node.oop_node:main",
            "publisher = basic_node.publisher:main",
            "simple_node = basic_node.simple_node:main",
            "subscriber = basic_node.subscriber:main",
            "number_publisher = basic_node.number_publisher:main",
            "number_counter = basic_node.number_counter:main",
        ],
    },
)
