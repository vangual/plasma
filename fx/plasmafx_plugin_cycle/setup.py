try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'plasmafx-plugin-cycle',
    version = '0.0.1',
    author = 'Philip Howard',
    author_email = 'phil@pimoroni.com',
    description = 'Colour cycle plugin for plasmafx',
    long_description = open('README.rst').read() + '\n' + open('CHANGELOG.txt').read(),
    license = 'MIT',
    keywords = 'plugin, effects, lighting',
    url = '',
    classifiers = [],
    packages = ['plasmafx_plugin_cycle'],
    entry_points = {
        'plasmafx.effect_plugins': [
            'Cycle = plasmafx_plugin_cycle:Cycle'
        ]
    }
)
