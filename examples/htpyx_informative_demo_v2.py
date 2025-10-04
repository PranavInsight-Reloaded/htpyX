#!/usr/bin/env python3
"""
htpyX Informative Demo v2 — improved design with hero, feature sections, and a fixed bottom counter.
Generates: htpyx_informative_demo_v2.html
Run from project root: python examples/htpyx_informative_demo_v2.py
"""

from css_generator import CSSBuilder
from htpyX_elements import Html, Head, Body, Div, H1, P, Button, Footer, Section, Title, Style, Span, H2, H3, tag
from htpyX_core import w, export_html
from pyXjs import reset

# reset any collected JS
reset()

# CSS: cleaner, more 'YouTube promo' style with gradients and large hero
css = CSSBuilder()
c...