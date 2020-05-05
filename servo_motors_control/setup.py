from setuptools import setup

package_name = 'servo_motors_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml', 'servo_motors_control.launch.py']),
    ],
    install_requires=[
        'setuptools',
        'Adafruit_PCA9685',
        'getch'],
    zip_safe=True,
    maintainer='Fumiya.Sato',
    maintainer_email='fumiya.sato.rop@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='servo mortors control using PCA9685 by jetson nano',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'key_control = ' + package_name + '.key_control:main',
            'servo_control = ' + package_name + '.servo_control:main',
        ],
    },
)
