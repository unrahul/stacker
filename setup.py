#!/usr/bin/env python

from setuptools import find_packages, setup  # type: ignore

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    author="unrahul",
    author_email="unrahul@unrahul.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="create stack dockerfiles from dockerfile templateyaml spec files",
    entry_points={"console_scripts": ["stacker=stacker.cli:main",],},
    install_requires=[],
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"stacker": ["py.typed"]},
    include_package_data=True,
    keywords="stacker",
    name="stacker",
    package_dir={"": "stacker"},
    packages=find_packages(include=["stacker", "stacker.*"]),
    setup_requires=["jinja","ruamel.yaml", "fire"],
    url="https://github.com/unrahul/stacker",
    version="0.1.0",
    zip_safe=False,
)
