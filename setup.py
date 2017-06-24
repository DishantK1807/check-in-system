from setuptools import setup

setup(
    name='Event',
    packages=['Event'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask-mysqldb', 'flask-session',
    ],
)