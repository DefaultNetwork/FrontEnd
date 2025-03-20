"""
Home.py
Landing page for the BetterSave Energy application
"""

import streamlit as st
import os
import base64
from imports_config import configure_page

# Import styling components after imports_config to avoid circular imports
from styles import apply_webflow_theme, render_navigation, render_footer, set_bg_from_local

def main():
    """Main landing page entry point"""
    # Configure the page
    configure_page()
    
    # Apply the Webflow theme
    apply_webflow_theme()
    
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
    
    # Navigation
    render_navigation()
    
    # **State Variables for Video Playback**
    if "play_video" not in st.session_state:
        st.session_state.play_video = False
    
    # ✅ **"EXPLORE MORE" Button**
    if st.button("EXPLORE MORE", key="explore"):
        st.session_state.play_video = True  # Set session state to trigger video
    
    # ✅ **Render Video & Close Button**
    if st.session_state.play_video:
        # Check if video file exists
        if os.path.exists("static/Final_video.MP4"):
            st.video("static/Final_video.MP4")  # Path to the video file inside static folder
        else:
            st.error("Video file not found. Please check the path: static/Final_video.MP4")
    
        # Close Video Button
        if st.button("CLOSE VIDEO", key="close"):
            st.session_state.play_video = False  # Stop playing the video
            st.rerun()  # Use the correct method to refresh the page
    
    # ✅ **Floating Email Button in Bottom-Right**
    st.markdown(
        '<a class="email-button" href="mailto:officialkhashayar@gmail.com">Write to Us</a>',
        unsafe_allow_html=True
    )
    
    # Footer
    render_footer()

if __name__ == "__main__":
    main()
