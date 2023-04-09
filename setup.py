#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="vibe-chart.py",
    version="1.0.1",
    description="Python API for downloading Naver Vibe charts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lou Park",
    author_email="gold24park@gmail.com",
    url="https://github.com/gold24park/vibe-chart.py",
    py_modules=["vibe"],
    license="MIT License",
    install_requires=["requests >= 2.28.2"],
)
