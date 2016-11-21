try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Do something when new story published to RSS',
    'author': 'Rob Denton',
    'url': 'https://github.com/registerguard/rssonpublish/',
    'download_url': 'https://github.com/registerguard/rssonpublish/',
    'author_email': 'rob.denton@registerguard.com',
    'version': '0.1',
    'install_requires': ['bitly-api','feedparser','oauthlib','py','pytest','requests','requests-oauthlib','six','tweepy'],
    'packages': ['onpublish','utilities'],
    #'scripts': ['bitly','rss','secrets','tweet'],
    'scripts': [],
    'name': 'RSSonpublish'
}

setup(**config)

