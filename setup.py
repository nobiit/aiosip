#!/usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'multidict>=2.0',
    'pyquery',
    'aiodns',
    'websockets',
    'async_timeout'
]

test_requirements = [
    'pytest',
    'pytest-asyncio'
]

setup(
    name='aiosip',
    version='1.0.3',
    description='SIP support for AsyncIO',
    long_description=readme + '\n\n' + history,
    author='DooPage',
    author_email='info@doopage.com',
    url='https://github.com/DooPage/aiosip',
    packages=[
        'aiosip',
    ],
    package_dir={'aiosip':
                     'aiosip'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache 2",
    zip_safe=False,
    keywords=['asyncio', 'sip', 'telephony'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
