# -*- coding: utf-8 -*-
#
# Automatically generated by nengo-bones, do not edit this file directly

import pathlib

import gyrus

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "nbsphinx",
    "nengo_sphinx_theme",
    "nengo_sphinx_theme.ext.backoff",
    "nengo_sphinx_theme.ext.sourcelinks",
    "notfound.extension",
    "numpydoc",
    "nengo_sphinx_theme.ext.autoautosummary",
    "nengo_sphinx_theme.ext.resolvedefaults",
    "sphinx.ext.inheritance_diagram",
]

# -- sphinx.ext.autodoc
autoclass_content = "both"  # class and __init__ docstrings are concatenated
autodoc_default_options = {"members": None}
autodoc_member_order = "bysource"  # default is alphabetical

# -- sphinx.ext.doctest
doctest_global_setup = """
import gyrus
import numpy as np
import matplotlib.pyplot as plt
"""

# -- sphinx.ext.intersphinx
intersphinx_mapping = {
    "nengo": ("https://www.nengo.ai/nengo/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "python": ("https://docs.python.org/3", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "sklearn": ("https://scikit-learn.org/dev", None),
}

# -- sphinx.ext.todo
todo_include_todos = True

# -- nbsphinx
nbsphinx_timeout = -1

# -- notfound.extension
notfound_template = "404.html"
notfound_urls_prefix = "/gyrus/"

# -- numpydoc config
numpydoc_show_class_members = False

# -- nengo_sphinx_theme.ext.sourcelinks
sourcelinks_module = "gyrus"
sourcelinks_url = "https://github.com/arvoelke/gyrus"

# -- sphinx
nitpicky = True
exclude_patterns = [
    "_build",
    "**/.ipynb_checkpoints",
]
linkcheck_timeout = 30
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
linkcheck_ignore = [r"http://localhost:\d+"]
linkcheck_anchors = True
default_role = "py:obj"
pygments_style = "sphinx"
user_agent = "gyrus"

project = "Gyrus"
authors = "Applied Brain Research"
copyright = "2021-2020 Applied Brain Research"
version = ".".join(gyrus.__version__.split(".")[:2])  # Short X.Y version
release = gyrus.__version__  # Full version, with tags

# -- HTML output
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "nengo_sphinx_theme"
html_title = f"Gyrus {release} docs"
htmlhelp_basename = "Gyrus"
html_last_updated_fmt = ""  # Default output format (suppressed)
html_show_sphinx = False
html_favicon = str(pathlib.Path("_static", "favicon.ico"))
html_theme_options = {
    "nengo_logo": "general-full-light.svg",
    "nengo_logo_color": "#a8acaf",
}
