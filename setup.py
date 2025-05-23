#!/usr/bin/env python
from setuptools import setup, find_namespace_packages

version = "1.0.2"

with open("./README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="backports_3_7.PyMySQL",
    version=version,
    url="https://github.com/pertsevds/backports_3_7.PyMySQL",
    project_urls={
        "Documentation": "https://pymysql.readthedocs.io/",
    },
    description="Pure Python MySQL Driver",
    long_description=readme,
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src',exclude=["backports_3_7.pymysql.tests*"]),
    python_requires=">=3.6",
    extras_require={
        "rsa": ["cryptography"],
        "ed25519": ["PyNaCl>=1.4.0"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
    ],
    keywords="MySQL",
)
