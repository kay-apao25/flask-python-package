import codecs

from setuptools import setup


tests_require = [
    # Pytest needs to come last.
    # https://bitbucket.org/pypa/setuptools/issue/196/
    'pytest',
    'factory-boy',
    'fake-factory',
]


install_requires = [
    'Flask==0.11.1',
    'flask-apispec==0.3.2',
    'Flask-JWT==0.3.2',
    'flake8',
    'coverage',
]


def long_description():
    with codecs.open('README.md', encoding='utf8') as f:
        return f.read()

setup(
    name='flask-python-package',
    version='0.1',
    description='A boilerplate for creating Flask Python packages',
    long_description=long_description(),
    url='https://github.com/kay-apao25/flask-python-package',
    download_url='https://github.com/kay-apao25/flask-python-package',
    author='Kay Apao',
    license=open('LICENSE').read(),
    include_package_data=True,
    packages=['scripts'],
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='test',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
    ],
)
