import os

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))


setup(
    name="dbc-custom-components",
    version="0.1.0",
    description="Example component built on top of dash-bootstrap-components",
    license="Apache Software License",
    author="Pascal Bugnion",
    author_email="pascal@bugnion.org",
    packages=find_packages(),
    install_requires=["dash>=0.32.1", "dash-bootstrap-components"],
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
