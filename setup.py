try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'iOS7 Lyrics Preview',
    'author': 'Bryce Matsuda',
    'url': 'https://github.com/KineticLiminality/ios7-lyrics-preview',
    'author_email': 'iexist4jcore@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lyrics_preview'],
    'scripts': [],
    'name': 'ios7-lyrics-preview'
}

setup(**config)
