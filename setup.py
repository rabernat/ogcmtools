try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Ocean GCM Tools',
    'author': 'Ryan Abernathey',
    'url': 'https://github.com/rabernat/ogcmtools',
    'download_url': 'https://github.com/rabernat/ogcmtools',
    'author_email': 'rpa@ldeo.columbia.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ogcmtools'],
    'scripts': [],
    'name': 'ogcmtools'
}

setup(**config)
