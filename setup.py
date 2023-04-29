from setuptools import setup, find_packages

setup(
    name="openalex-works",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": ["openalex-works=openalex_works.cli:main"],
    },
)
