# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Maivin User Manual'
copyright = '2024, Au-Zone Technologies'
author = 'Au-Zone Technologies'
release = '2024Q4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinx.ext.githubpages",
    "sphinx_multiversion",
    "sphinx_rtd_dark_mode",
]

myst_fence_as_directive = ["mermaid"]
myst_enable_extensions = ["attrs_inline"]
mermaid_cmd = "./node_modules/.bin/mmdc"

templates_path = ['templates']
include_patterns = ['*.rst', '*.md']
exclude_patterns = ['README.*', 'build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False
html_static_path = ['static']
html_css_files = ['css/maivin.css']
html_logo = 'static/maivin.png'
html_context = {
    'default_mode': 'dark'
}

latex_logo = 'static/maivin_cover.png'
latex_elements = {
    # The paper size ('letter' or 'a4').
    'papersize': 'letter'
}
