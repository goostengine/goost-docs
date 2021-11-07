# -*- coding: utf-8 -*-
#
# Goost documentation build configuration file

import sys
import os

# -- Project information -----------------------------------------------------

project = "Goost"
copyright = "2019-2021, Andrii Doroshenko and the Goost community (CC-BY 3.0)"
author = "Andrii Doroshenko and the Goost community"

version = os.getenv("READTHEDOCS_VERSION", "1.1-gd3")
release = version

goost_branch = version
if version == "latest":
    goost_branch = "gd3"

godot_map = {
    # Goost : Godot
    "latest" : "3.4",
    "gd3": "3.4",
    "1.1-gd3": "3.4",
    "gd4": "latest",
}
godot_docs_url = "https://docs.godotengine.org/en/%s/" % (godot_map[version])

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.imgmath",
    "sphinx_tabs.tabs",
]

templates_path = ["_templates"]
source_suffix = [".rst", ".md"]
master_doc = "index"
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", ".github"]

# Syntax highlighting
from sphinx.highlighting import lexers
from pygments.lexers import GDScriptLexer

lexers["gdscript"] = GDScriptLexer()
pygments_style = "sphinx"
highlight_language = "gdscript"

# Define common substitutions
rst_prolog = """
.. |goost_branch| replace:: {goost_branch}
.. |godot_branch| replace:: {godot_branch}
""".format(
    goost_branch=goost_branch, 
    godot_branch=godot_map[version]
)

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_logo = "img/logo.png"

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    "logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "style_nav_header_background": "#343131",  # Match sidebar background.
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "goostengine",  # Username
    "github_repo": "goost-docs",  # Repo name
    "github_version": version,  # Version
    "conf_py_path": "/",  # Path in the checkout to the docs root
}

html_static_path = ["_static"]
html_extra_path = ["robots.txt"]
html_css_files = ["css/custom.css"]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Goostdoc"

# -- Options for LaTeX output ------------------------------------------------

latex_documents = [
    (
        master_doc,
        "Goost.tex",
        "Goost Documentation",
        "Andrii Doroshenko and the Goost community",
        "manual",
    ),
]

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Goost uses Godot atomic datatypes and classes, so provide an external URI
# to the Godot API to have valid links throughout the class reference.
intersphinx_mapping = {godot_docs_url: None}
