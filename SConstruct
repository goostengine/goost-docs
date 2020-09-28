#!/usr/bin/env python

import pickle
import methods

env = Environment()
env.__class__.SphinxBuild = methods.sphinx_build
env.__class__.GetTargetBuildDir = methods.get_target_build_dir

env["supported_targets"] = {
    "html":       "standalone HTML files",
    "dirhtml":    "HTML files named index.html in directories",
    "singlehtml": "a single large HTML file",
    "pickle":     "pickle files",
    "json":       "JSON files",
    "htmlhelp":   "HTML files and a HTML help project",
    "qthelp":     "HTML files and a qthelp project",
    "applehelp":  "an Apple Help Book",
    "devhelp":    "HTML files and a Devhelp project",
    "epub":       "an epub",
    "latex":      "LaTeX files",
    "latexpdf":   "LaTeX files and run them through pdflatex",
    "latexpdfja": "LaTeX files and run them through platex/dvipdfmx",
    "text":       "text files",
    "man":        "manual pages",
    "texinfo":    "Texinfo files",
    "info":       "Texinfo files and run them through makeinfo",
    "gettext":    "PO message catalogs",
    "changes":    "an overview of all changed/added/deprecated items",
    "xml":        "Docutils-native XML files",
    "pseudoxml":  "pseudoxml-XML files for display purposes",
}

opts = Variables()
opts.Add("target", "Documentation build format (%s)" % ",".join(env["supported_targets"].keys()), "html", validator=methods.validate_target)
opts.Add("build_dir", "The directory in which you want to place the built documentation", "_build")

opts.Update(env)
Help(opts.GenerateHelpText(env))

skip_build = False

if GetOption("help"):
    skip_build = True
elif GetOption("clean"):
    Execute(Delete(env.GetTargetBuildDir()))
    skip_build = True

# Build the documentation.
if not skip_build:
    env.SphinxBuild()

# Avoid issues when building with different
# versions of Python out of the same directory.
env.SConsignFile(".sconsign{0}.dblite".format(pickle.HIGHEST_PROTOCOL))
