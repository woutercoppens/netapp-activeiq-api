# -*- coding: utf-8 -*-
# ===========================
# Setup file
# ===========================

import re
from setuptools import setup, find_packages


version = re.search(
    r'__version__\s*=\s*"(.+)"', open("netapp_activeiq_api/__init__.py", "rt").read()
).group(1)

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="netapp-activeiq-api",
    version=version,
    author="Wouter Coppens",
    author_email="wouter.coppens@proact.eu",
    description="This package allows to consume the NetApp ActiveIQ API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woutercoppens/netapp-activeiq-api",
    packages=find_packages(exclude=["samples"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    python_requires=">=3.8",
)
