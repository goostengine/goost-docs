# -*- coding: utf-8 -*-
#
# Goost documentation build configuration file

import sys
import os

# -- Project information -----------------------------------------------------

project = "Goost"
copyright = "2020, Andrii Doroshenko and the Goost community (CC-BY 3.0)"
author = "Andrii Doroshenko and the Goost community"

# Version info for the project, acts as replacement for |version| and |release|
# The short X.Y version
version = os.getenv("READTHEDOCS_VERSION", "latest")
# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"
highlight_language = "gdscript"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_logo = "img/logo.png"

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    "logo_only": True,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
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
    "github_user": "GoostGD",  # Username
    "github_repo": "goost-docs",  # Repo name
    "github_version": "gd3",  # Version
    "conf_py_path": "/",  # Path in the checkout to the docs root
}

html_static_path = ["_static"]

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

# intersphinx_mapping = {'https://docs.godotengine.org/': None}
