try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'plasmafx',
    version = '0.0.1',
    author = 'Philip Howard',
    author_email = 'phil@pimoroni.com',
    description = 'LED effects sequencer for Plasma Arcade Button Lights',
    long_description = open('README.rst').read() + '\n' + open('CHANGELOG.txt').read(),
    license = 'MIT',
    keywords = 'plugin, effects, lighting',
    url = '',
    classifiers = [],
    packages = ['plasmafx'],
)
