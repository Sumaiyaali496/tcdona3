# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tcdona3'
copyright = '2024, Agastya Raj'
author = 'Agastya Raj'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import os
import sys

# Add your project root directory to the Python path
sys.path.insert(0, os.path.abspath('.'))

# Check if we're on Read the Docs' build environment
on_rtd = os.environ.get('READTHEDOCS') == 'True'

# Use the correct output path on Read the Docs
if on_rtd:
    html_output_path = os.environ.get('READTHEDOCS_OUTPUT', '')
    if html_output_path:
        html_output_dir = os.path.join(html_output_path, 'html')
        # Make sure the directory exists
        os.makedirs(html_output_dir, exist_ok=True)
        html_static_path = [html_output_dir]
    else:
        html_static_path = ['_static']
else:
    html_static_path = ['_static']

# Ensure the path is correct for the Read the Docs en
html_theme = 'alabaster'
#html_static_path = ['_static']
