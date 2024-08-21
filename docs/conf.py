# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from unittest.mock import MagicMock

# Mocking imports to avoid installing heavy dependencies
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return MagicMock()

# List of modules to mock
MOCK_MODULES = ['pandas','mysql.connector']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

sys.path.insert(0, os.path.abspath('../'))

project = 'tcdona3'
copyright = '2024, Agastya Raj'
author = 'Agastya Raj'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
