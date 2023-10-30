import setuptools
from setuptools import find_packages, setup

setuptools.setup(name="discord-music-bot", packages=find_packages())


setup(
    name="discord-music-bot",
    version="0.1.0",
    author="Jack Sparrow",
    author_email="Dont@spam.me",
    description="A discord music bot",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/esocoding/discord-music-bot",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=open("requirements.txt").readlines(),
    test_suite="tests",
)
