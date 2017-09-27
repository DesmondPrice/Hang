#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="hang",
    version="0.0.0",
    author="Artem Zharinov",
    author_email="ortemko@list.ru",
    url="https://github.com/DesmondPrice/Hang.git",
    license="MIT",
    packages=[
        "bin",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)