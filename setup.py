try:
	from setuptools import setup
except ImportErrpr:
        from distutils.core import setup


confif = {
        'description': 'exec',
        'author': 'DongQibai',
        'url': 'http://192.168.234.130/',
        'download_url': 'http://192.168.234.130',
        'author_email': 'dongqibai@hongkun.com',
        'version': '1.0',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [''],
        'name': 'exec'
}


setup(**config)
