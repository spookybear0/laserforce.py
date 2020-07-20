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
    "sphinxcontrib_trio",
    # "rst2pdf.pdfbuilder",
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
copyright = "2019-2020, SpookyBear0"

version = ""
with open("../laserforce/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

release = version

language = "en"

pdf_documents = [
    (
        "index",
        "Laserforce.py Documentation",
        "laserforce.py documentation, built with PDF format.",
        "SpookyBear0",
    )
]

exclude_patterns = ["build"]

pygments_style = "friendly"  # we need to use "monokai" for dark theme I think ~ nekit

html_theme = "sphinx_rtd_theme"
