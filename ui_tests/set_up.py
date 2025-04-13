from setuptools import setup, find_packages


setup(
    name='ui_tests',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'appium-python-client',
        'behave',
        'pytest',
        'selenium'
    ]
)