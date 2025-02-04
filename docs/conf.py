project = 'lukenet'
copyright = '2025, Luke Keyte'
author = 'Luke Keyte'
release = '1.0'

extensions = [
    'myst_parser',
    'sphinx.ext.mathjax'
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence"
]

myst_update_mathjax = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_depth': 2,  # Only show top level
    'collapse_navigation': False,  # Optional: controls if navigation entries should be collapsed
}


html_static_path = ['_static']

# Enable numbering for headers
myst_heading_anchors = 3