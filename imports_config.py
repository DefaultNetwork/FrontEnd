"""
imports_config.py
Contains all imports and basic configuration for the BetterSave Energy Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import numpy as np
import calendar
import os
import time

# Define colors directly in imports_config to avoid circular imports
# NOTE: These same colors are duplicated in styles.py for consistency
# DO NOT import from styles.py here to avoid circular dependencies
COLORS = {
    # Core theme colors from Webflow theme
    "neutral_800": "#080f25",     # Dark background
    "neutral_700": "#212c4d",     # Dark secondary
    "neutral_600": "#37446b",     # Dark border
    "neutral_500": "#7e89ac",     # Medium text
    "neutral_400": "#aeb9e1",     # Light text
    "neutral_300": "#d1dbf9",     # Very light text
    "neutral_200": "#d9e1fa",     # Almost white
    "neutral_100": "#ffffff",     # White

    # Accent colors
    "primary": "#6c72ff",         # Main accent
    "secondary": "#57c3ff",       # Secondary accent
    "tertiary": "#9a91fb",        # Tertiary accent
    "accent": "#fdb52a",          # Accent highlight
    "dark_accent": "#101935",     # Dark accent background
    "neutral_accent": "#343b4f",  # Neutral accent

    # System feedback colors
    "success": "#14ca74",         # Success/positive
    "error": "#ff5a65",           # Error/negative
    "red_400": "#dc2b2b",         # Deep error

    # Derived/utility colors
    "bg_primary": "#101935",      # Primary background
    "bg_transparent": "rgba(16, 25, 53, 0)",  # Transparent background
    "grid": "rgba(55, 68, 107, 0.5)",         # Grid lines with transparency
}

# Set page configuration
def configure_page():
    """Configure the Streamlit page settings"""
    st.set_page_config(
        page_title="BetterSave Energy Dashboard",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )

# Define plot theme configuration to match Webflow dark theme
PLOT_THEME = {
    "template": "plotly_dark",
    "plot_bgcolor": COLORS["bg_primary"],
    "paper_bgcolor": COLORS["bg_transparent"],
    "font_color": COLORS["neutral_400"],
    "grid_color": COLORS["grid"],
    "color_sequence": [
        COLORS["primary"],
        COLORS["secondary"],
        COLORS["tertiary"],
        COLORS["accent"],
        COLORS["neutral_accent"]
    ]
}
