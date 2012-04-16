import os
from distutils.core import setup

def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)
    return open(path).read()

setup(name='blekko',
      version='0.1',
      description='bindings for the Blekko search engine API',
      author='Adrian Sampson',
      author_email='adrian@radbox.org',
      url='https://github.com/sampsyo/python-blekko',
      license='MIT',
      platforms='ALL',
      long_description=_read('README.rst'),

      py_modules=['blekko'],

      classifiers=[
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2',
      ],
)
