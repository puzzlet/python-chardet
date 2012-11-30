import sys
from setuptools import setup

# Patch distutils if it can't cope with the "classifiers"
# keyword (prior to python 2.3.0):
from distutils.dist import DistributionMetadata
if not hasattr(DistributionMetadata, 'classifiers'):
    DistributionMetadata.classifiers = None

kwargs = {}
if sys.version_info >= (3, ):
    kwargs['use_2to3'] = True
setup(
    name='chardet',
    version='2.1.1',
    description='Universal encoding detector',
    long_description=open('README.rst').read(),
    author='Mark Pilgrim',
    author_email='mark@diveintomark.org',
    url='https://github.com/erikrose/chardet',
    license="LGPL",
    platforms=['POSIX', 'Windows'],
    keywords=['encoding', 'i18n', 'xml'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.3",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    scripts=['bin/chardetect.py'],
    packages = ['chardet'],
    **kwargs
    )
