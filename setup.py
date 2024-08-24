from setuptools import setup, find_packages

setup(
    name='ccwc',
    version='1.0',
    description='A command-line tool for counting characters, words, and lines in a file or standard input',
    url='https://github.com/VaishnavSherla/ccwc',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ccwc = ccwc.main:main',
        ],
    },
    python_requires='>=3.6',
)