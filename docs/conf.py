import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'lukenet'
copyright = '2025, Luke Keyte'
author = 'Luke Keyte'
release = '1.0'

extensions = ['myst_parser']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']