from setuptools import setup

setup(
    name='TicTacToe',
    packages=['web_app', 'app'],
    include_package_data=True,
    install_requires=['flask'],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    )
