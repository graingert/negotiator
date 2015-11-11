from setuptools import setup, find_packages

readme = open('README.rst').read()
history = open('CHANGES.rst').read().replace('.. :changelog:', '')

setup(
    name='negotiator',
    version='1.0.0',
    packages=find_packages(exclude='tests'),
    install_requires=[],
    url='https://github.com/CottageLabs/negotiator',
    author='Richard Jones',
    author_email='richard@cottagelabs.com',
    description='Proper Content Negotiation for Python',
    license='CC0',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
