from setuptools import setup, find_packages

setup(
    name='swetrackapi',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='API for SweTrack Live Tracking cloud platform. swetrack.com',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/oeysteinhansen/pyswetrack',
    author='Øystein Hansen',
    author_email='oeysteinhansen@gmail.com',
    test_suite='nose.collector',
    tests_require=['nose'],
)
