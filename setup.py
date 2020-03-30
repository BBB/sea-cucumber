from setuptools import setup

DESCRIPTION = "A Django email backend for Amazon Simple Email Service, backed by celery."

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='seacucumber-py3',
    version='1.6.0',
    packages=[
        'seacucumber',
        'seacucumber.management',
        'seacucumber.management.commands',
    ],
    author='Ollie Relph',
    author_email='ollie@relph.me',
    url='https://github.com/BBB/sea-cucumber/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=['boto>=2.25.0', 'celery'],
)
