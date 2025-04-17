import os
import sys

# Minimal required Sphinx settings
project = 'pysal'
copyright = '2025'
author = 'pysal'

# Required Sphinx stubs
extensions = []
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Theme doesn't matter as its output will be overwritten
html_theme = 'alabaster'