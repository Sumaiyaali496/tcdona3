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


# Ensure the path is correct for the Read the Docs environment
on_rtd = os.environ.get('READTHEDOCS') == 'True'

if on_rtd:
    # Set the output directory for HTML files
    html_output_path = os.path.join(os.environ.get('READTHEDOCS_OUTPUT', ''), 'html')
    if not os.path.exists(html_output_path):
        os.makedirs(html_output_path)
    html_static_path = [html_output_path]

html_theme = 'alabaster'
html_static_path = ['_static']
