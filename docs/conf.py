import os
import sys


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'embdgen'
copyright = '2024, AOX Technologies GmbH, Elektrobit Automotive GmbH'
author = 'AOX Technologies GmbH, Elektrobit Automotive GmbH'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.append(os.path.abspath("./_ext"))
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "config",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_off']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['css/custom_theme.css']

_exclude_members = []

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "member-order": "bysource",
    "exclude-members": ",".join(_exclude_members)
}


# Disable update_annotation, this breaks the build, because it changes
# __annotations__ and this is used by embdgen to generate meta information
from sphinx.ext.autodoc import AttributeDocumenter
def noop(*args, **kwargs): pass
AttributeDocumenter.update_annotations = noop

