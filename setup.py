"""
Publish a new version:
$ git tag X.Y.Z -m "Release X.Y.Z"
$ git push --tags
$ pip install --upgrade twine wheel
$ python setup.py sdist bdist_wheel --universal
$ twine upload dist/*
"""
import codecs
from setuptools import setup


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()


setup(
    name='enabling-ros2-warnings-tools',
    packages=['enabling_ros2_warnings_tools'],
    version='0.0.1',
    description='Streamline the process of adding warnings to ROS2 packages',
    long_description=read_file('README.rst'),
    license='MIT',
    author='Audrow Nash',
    author_email='audrow@hey.com',
    url='https://github.com/audrow/ros2-workflow-tools',
    keywords=[
        'ros2', 'productivity',
    ],
    install_requires=[
    ],
    tests_require=[
        'flake8',          # check code style for pep-8
        'pep257',  # test the doc strings
        'pytest',  # a testing framework
        'pytest-cov',  # for code coverage
        'pytest-mock',  # mocks for pytest
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Natural Language :: English',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'make_warning_pr = enabling_ros2_warnings_tools.create_warning_pr:main',
        ],
    },
)
