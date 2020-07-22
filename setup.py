from setuptools import setup
import pathlib

setup(name="laserforce.py",
      version="1.0.01",
      description="Python package for laserforce.",
      long_description=(root / "README.rst").read_text("utf-8"),
      author="SpookyBear0",
      author_email="collinmcarroll@gmail.com",
      packages=["laserforce"],
      zip_safe=False,
      )
