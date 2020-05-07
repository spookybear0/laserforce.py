import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="laserforce.api",
    version="1.0.2",
    author="SpookyBear0",
    author_email="collinmcarroll@gmail.com",
    description="An API for Laserforce in python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpookyBear0/laserforce.api",
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
)