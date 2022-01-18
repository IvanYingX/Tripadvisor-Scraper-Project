from setuptools import setup
from setuptools import find_packages

setup(
    name='tripadvisor_scraper',
    version='0.0.1',
    description='Mock package that scrap data of hotels from Tripadvisor',
    author='dhaval_luqman_aicore',
    license='MIT',
    packages=find_packages(),
    install_requires=['selenium','sqlalchemy'],




)