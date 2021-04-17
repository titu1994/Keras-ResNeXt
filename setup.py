#!/usr/bin/env python

import os

from setuptools import find_packages, parse_requirements, setup

_PATH_ROOT = os.path.dirname(__file__)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="resnext-keras",
    version="0.1",
    author="Somshubra Majumdar",
    author_email="titu1994@gmail.com",
    description="Implementation of ResNeXt models for Keras 2.0+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/titu1994/Keras-ResNeXt",
    project_urls={
        "Bug Tracker": "https://github.com/titu1994/Keras-ResNeXt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    setup_requires=[],
    install_requires=parse_requirements('requirements.txt')
)
