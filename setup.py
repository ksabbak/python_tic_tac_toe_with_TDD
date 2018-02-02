from setuptools import setup

setup(
    name='tictactoe',
    packages=[
        'tictactoe',
        'tictactoe.web_app',
        'tictactoe.app',
        'tictactoe.app.models',
        'tictactoe.tests'
        ],
    include_package_data=True,
    install_requires=['flask'],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    )
