# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import setuptools
cfg = setuptools.config.read_configuration(r'..\setup.cfg')

project = cfg["metadata"]["name"]
version = cfg["metadata"]["version"]
# copyright = '2021, Author Name'
author = '{{cookiecutter.full_name}}'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    #"IPython.sphinxext.ipython_console_highlighting",
    #"nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]

# This is autosummary configuration stuff
autosummary_generate = True
autoclass_content = "both"
add_module_names = False
autosummary_imported_members = True
autodoc_default_options = {
    "members": True,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_logo = "_static/ChalmersU_black.png"

html_theme_options = {
    # "announcement": "<em>Important</em> announcement!",
    "light_logo": "ChalmersU_black.png",
    "dark_logo": "ChalmersU_white.png",
    
    "light_css_variables": {
        "color-brand-primary": "#006C5C",# "#00A99D", 
        "color-brand-content": "#006C5C",

        # to change the sidebar to grey. WIP because many things need to change 
        "color-background-hover": "#dbdbdb",
        "color-sidebar-background": "#d0d0d0", 

        "color-guilabel-background": "#dddddd",

        # Admonitions
        # --- Color: Tile (Orange)
        "color-admonition-title--danger": "rgba(241,90,34,1)", 
        "color-admonition-title-background--danger": "rgba(241,90,34,0.1)",
        "color-admonition-title--attention": "rgba(241,90,34,1)", 
        "color-admonition-title-background--attention": "rgba(241,90,34,0.1)",
        "color-admonition-title--error": "rgba(241,90,34,1)", 
        "color-admonition-title-background--error": "rgba(241,90,34,0.1)",
        # --- Color: Energy (yellow)
        "color-admonition-title--caution": "rgba(255,203,5,1)", 
        "color-admonition-title-background--caution": "rgba(255,203,5,0.1)",
        "color-admonition-title--warning": "rgba(255,203,5,1)", 
        "color-admonition-title-background--warning": "rgba(255,203,5,0.1)",        
        # --- Color: Blue sky
        "color-admonition-title--note": "rgba(88,176,227,1)", 
        "color-admonition-title-background--note": "rgba(88,176,227,0.1)",
        "color-admonition-title--seealso": "rgba(88,176,227,1)", 
        "color-admonition-title-background--seealso": "rgba(88,176,227,0.1)",
        # --- Color: Dark Copper (Green)
        "color-admonition-title--important": "rgba(0,108,92,1)", 
        "color-admonition-title-background--important": "rgba(0,108,92,0.1)",
        # --- Color: Copper (Bright Green)
        "color-admonition-title--hint": "rgba(0,169,157,1)", 
        "color-admonition-title-background--hint": "rgba(0,169,157,0.1)",
        "color-admonition-title--tip": "rgba(0,169,157,1)", 
        "color-admonition-title-background--tip": "rgba(0,169,157,0.1)",
        # --- Color: Dusk (Blue)
        "color-admonition-title--important": "rgba(39,0,137,1)", 
        "color-admonition-title-background--important": "rgba(39,0,137,0.1)",
    },
    "dark_css_variables": {
        "color-brand-primary": "#F15A22",
        "color-brand-content": "#F15A22",


        # This is here because the I changed the sidebar to grey, and it changes in
        # both light and dark themes
        "color-sidebar-background": "#000000",

    }
}

# CHALMERS IDENTITY COLORS
#  Hex   R,G,B      Name SWE      Name ENG      
# ------ ---------- -----------   -----------
# 006C5C 0,108,92   Dark Copper   Mork Koppar
# 00A99D 0,169,157  Copper        Koppar
# 7FB539 127,181,57 Leaf          Lov
# 5D6F7A 93,111,122 Granite       Granit
# 58B0E3 88,176,227 Sky           Himmel
# 483729 72,55,41   Coffee        Kaffe
# F15A22 241,90,34  Tiles         Tegel
# FFCB05 255,203,5  Energy        Energi
# 003050 0,48,80    West Coast    Vastkust
# 270089 39,0,137   Dusk          Skymning