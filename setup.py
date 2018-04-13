import codecs
from setuptools import setup, find_packages

setup(name='xlingcorrelation',
      version='0.1',
      description='correlation CDS/CDI',
      url='https://github.com/bootphon/XLingCorrelation',
      author='GladB',
      author_email='gladys.baudet@gmail.com',
      license='',
      long_description=codecs.open('README.md', encoding='utf-8').read(),
      packages=find_packages(),
      installs_requires=['pandas','subprocess','numpy','re','scipy','sklearn','zip']
      zip_safe=False)
