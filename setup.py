from setuptools import setup
import pathlib

root = pathlib.Path(__file__).parent

setup(
    name="laserforce.py",
    version="2.1.0",
    description="A python package for interacting with iplaylaserforce.com.",
    long_description=(root / "README.md").read_text("utf-8"),
    author="spookybear0",
    author_email="chloecarroll103@gmail.com",
    packages=["laserforce"],
    zip_safe=False
)
