"""
stacker
--------
splice and slice dockerfiles
"""

from distutils.core import setup

setup(
    name="stacker",
    version="0.0.1",
    description="splice and slice dockerfiles",
    author="unrahul",
    license="Apache license 2.0",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache license 2.0",
        "Intended Audience :: Developers",
        "Topic :: Containers",
    ],
    py_modules=["stacker.stacker"],
)
