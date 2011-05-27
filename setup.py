"""
Flask-Solr
----------

Adds Solr support to your Flask application.
"""

from setuptools import setup


setup(
    name='Flask-Solr',
    version='0.1',
    license='BSD',
    author='WillowTree Apps',
    author_email='ron.duplain@willowtreeapps.com',
    description='Adds Solr support to your Flask application',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'pysolr',
        'Flask',
    ],
    # test_suite='test_solr.suite',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
