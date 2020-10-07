import setuptools
from distutils.core import Extension

with open("README.md") as f:
    long_description = f.read()

with open("./src/pygictower/__init__.py") as f:
    for line in f.readlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            break
    else:
        print("Can't find version! Stop Here!")
        exit(1)

setuptools.setup(
    name="pygictower",
    version=version,
    author="Tian Gao",
    author_email="gaogaotiantian@hotmail.com",
    description="Python based AI game platform inspired by magic tower",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaogaotiantian/pygictower",
    packages=setuptools.find_packages("src"),
    package_dir={"":"src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires=">=3.6",
)
