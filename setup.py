from setuptools import setup
import pathlib

root = pathlib.Path(__file__).parent

setup(
    name="laserforce.py",
    version="2.0.0",
    description="Python package for laserforce.",
    long_description=(root / "README.md").read_text("utf-8"),
    author="spookybear0",
    author_email="collinmcarroll@gmail.com",
    packages=["laserforce"],
    zip_safe=False
)
