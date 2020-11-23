from setuptools import setup, find_packages

setup(
    name='c4-achitecture',
    version='0.1dev',
    install_requires=[
        'graphviz'
    ],
    packages=find_packages(),
    license='MIT',
    long_description=open('README.md').read(),
    url='https://github.com/jieyinybl/c4-architecture.git',
    author='JieyingYan'
)
