import re
import os
import sys

sys.path.insert(0, os.path.abspath(".."))
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autodoc_member_order = "bysource"

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aio": ("https://aiohttp.readthedocs.io/en/stable/", None),
}

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

source_suffix = ".rst"

master_doc = "index"

project = "laserforce.py"
copyright = "2025, spookybear0"

language = "en"

pdf_documents = [
    (
        "index",
        "Laserforce.py Documentation",
        "laserforce.py documentation, built with PDF format.",
        "spookybear0",
    )
]

exclude_patterns = ["build"]

pygments_style = "friendly"

html_theme = "sphinx_rtd_theme"
