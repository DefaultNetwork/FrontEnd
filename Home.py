"""
Home.py
Landing page for the BetterSave Energy application
"""

import streamlit as st
import os
import base64
from imports_config import configure_page

# Import styling components after imports_config to avoid circular imports
from styles import apply_webflow_theme, render_footer, render_logo, set_bg_from_local

def render_home_sidebar():
    """Render a simplified sidebar for the home page"""
    with st.sidebar:
        # Logo
        render_logo()

        st.markdown("### Welcome to BetterSave")

        st.markdown("""
        Explore our energy dashboard to see how we're helping
        optimize renewable energy distribution across Germany.
        """)

        st.markdown("---")

        # Navigation links (since we removed the top navbar)
        st.markdown("### Navigation")

        if st.button("🏠 Home", type="primary"):
            st.switch_page("Home.py")

        if st.button("🔍 Dashboard"):
            st.switch_page("Pages/Dashboard.py")

        if st.button("📊 Predictions"):
            st.switch_page("Pages/Prediction.py")

        if st.button("ℹ️ About Us"):
            st.switch_page("Pages/About.py")

        st.markdown("---")
        st.markdown("<div class='footer'>BetterSave Energy Analytics Platform</div>", unsafe_allow_html=True)

def main():
    """Main landing page entry point"""
    # Configure the page
    configure_page()

    # Apply the Webflow theme
    apply_webflow_theme()

    # Render simplified sidebar
    render_home_sidebar()

    # Check if the static directory and background image exist
    if os.path.exists("static/BK1.jpg"):
        # Set background image with overlay
        set_bg_from_local("static/BK1.jpg")  # Path to the background image in static folder
    else:
        # Fallback dark background if image is not found
        st.markdown("""
            <style>
            .stApp {
                background-color: #080f25;
            }
            </style>
        """, unsafe_allow_html=True)
        st.warning("Background image not found. Using default background.")

    # Main content - removed navigation bar to give unobstructed view
    st.markdown("<h1 class='main-header'>BetterSave Energy</h1>", unsafe_allow_html=True)
    st.markdown("<p class='center-text' style='font-size: 1.5rem;'>Intelligent Energy Storage and Distribution</p>", unsafe_allow_html=True)

    # Add some spacing to center the content vertically
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    # **State Variables for Video Playback**
    if "play_video" not in st.session_state:
        st.session_state.play_video = False

    # ✅ **"EXPLORE MORE" Button**
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("EXPLORE MORE", key="explore", use_container_width=True):
            st.session_state.play_video = True  # Set session state to trigger video

    # ✅ **Render Video & Close Button**
    if st.session_state.play_video:
        # Check if video file exists
        if os.path.exists("static/Final_video.MP4"):
            st.video("static/Final_video.MP4")  # Path to the video file inside static folder
        else:
            st.error("Video file not found. Please check the path: static/Final_video.MP4")

        # Close Video Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("CLOSE VIDEO", key="close", use_container_width=True):
                st.session_state.play_video = False  # Stop playing the video
                st.rerun()  # Use the correct method to refresh the page

    # ✅ **Floating Email Button in Bottom-Right**
    st.markdown(
        '<a class="email-button" href="mailto:officialkhashayar@gmail.com">Write to Us</a>',
        unsafe_allow_html=True
    )

    # Footer - smaller and less obtrusive for the home page
    st.markdown("""
        <div class='footer' style='margin-top: 100px; opacity: 0.7;'>
            © 2025 BetterSave Energy • Making Energy Management Smarter
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
