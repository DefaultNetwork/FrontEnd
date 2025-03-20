"""
Home.py
Landing page for the BetterSave Energy application
"""

import streamlit as st
from imports_config import configure_page
from styles import apply_webflow_theme, render_navigation, render_footer, set_bg_from_local

# **Apply standard theme**
def main():
    """Main landing page entry point"""
    # Configure the page
    configure_page()
    
    # Apply the Webflow theme
    apply_webflow_theme()
    
    # Set background image with overlay
    set_bg_from_local("static/BK1.jpg")  # Path to the background image in static folder
    
    # **State Variables for Video Playback**
    if "play_video" not in st.session_state:
        st.session_state.play_video = False
    
    # ✅ **"EXPLORE MORE" Button**
    if st.button("EXPLORE MORE", key="explore"):
        st.session_state.play_video = True  # Set session state to trigger video
    
    # ✅ **Render Video & Close Button**
    if st.session_state.play_video:
        st.video("static/Final_video.MP4")  # Path to the video file inside static folder
    
        # Close Video Button
        if st.button("CLOSE VIDEO", key="close"):
            st.session_state.play_video = False  # Stop playing the video
            st.rerun()  # Use the correct method to refresh the page
    
    # ✅ **Floating Email Button in Bottom-Right**
    st.markdown(
        '<a class="email-button" href="mailto:officialkhashayar@gmail.com">Write to Us</a>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
