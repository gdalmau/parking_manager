from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.readlines()

setup(
    name='parking_manager',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/gdalmau/parking_manager',
    license='MIT',
    author='Gerard Dalmau',
    description='Parking manager',
    install_requires=INSTALL_REQUIRES
)
