import streamlit as st
import base64

# Set page config directly (no imports needed)
st.set_page_config(page_title="BetterSave", layout="wide")

# Function to Set Full-Page Background Image with Dark Overlay
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Dark overlay for readability */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.4); /* Semi-transparent black */
            z-index: -1;
        }}

        /* Ensure text is readable */
        .stText, .stMarkdown, h1, h2, h3 {{
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            text-align: center;
        }}

        /* Center the buttons */
        .btn-container {{
            display: flex;
            justify-content: center;
            margin-top: 50px;
            gap: 20px;
        }}

        /* Button styling */
        .custom-btn {{
            font-size: 20px;
            font-weight: bold;
            color: white !important;
            text-decoration: none;
            padding: 12px 25px;
            border: 2px solid white;
            border-radius: 5px;
            transition: 0.3s ease-in-out;
            animation: blink 1.5s infinite; /* Slower blinking */
            background-color: transparent;
            cursor: pointer;
            position: relative;
        }}

        /* Green glowing effect */
        .custom-btn::before {{
            content: "";
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            border-radius: 5px;
            background: linear-gradient(45deg, #00ffcc, #00ffcc, #00ffcc, #00ffcc);
            z-index: -1;
            opacity: 0;
            animation: glow 3s infinite; /* Slow glowing effect */
        }}

        /* Slower blinking animation */
        @keyframes blink {{
            0% {{ background-color: white; color: black; }}
            50% {{ background-color: black; color: white; }}
            100% {{ background-color: white; color: black; }}
        }}

        /* Glowing animation */
        @keyframes glow {{
            0% {{ opacity: 0; box-shadow: 0 0 5px #00ffcc; }}
            50% {{ opacity: 1; box-shadow: 0 0 20px #00ffcc; }}
            100% {{ opacity: 0; box-shadow: 0 0 5px #00ffcc; }}
        }}

        /* Hover Effect */
        .custom-btn:hover {{
            animation: none; /* Stop blinking on hover */
            background-color: rgba(255, 255, 255, 0.2);
        }}

        .custom-btn:hover::before {{
            opacity: 1; /* Show glow on hover */
        }}

        /* Floating Email Button */
        .email-button {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: white;
            color: black;
            font-size: 16px;
            font-weight: bold;
            padding: 12px 20px;
            border-radius: 5px;
            text-align: center;
            text-decoration: none;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            border: 2px solid black;
            transition: 0.3s ease-in-out;
        }}

        .email-button:hover {{
            background-color: black;
            color: white;
            transform: scale(1.05);
        }}

        /* Sidebar styling */
        .sidebar-navigation {{
            background-color: rgba(33, 44, 77, 0.6);
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}

        .sidebar-link {{
            display: block;
            padding: 10px;
            margin-bottom: 5px;
            background-color: rgba(108, 114, 255, 0.3);
            color: white !important;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            transition: all 0.3s ease;
        }}

        .sidebar-link:hover {{
            background-color: rgba(108, 114, 255, 0.7);
            transform: translateX(5px);
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# Create simple logo for sidebar
def render_logo():
    st.sidebar.markdown("""
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <div style="background: linear-gradient(135deg, #6c72ff, #57c3ff); width: 80px; height: 80px;
                  border-radius: 16px; display: flex; align-items: center; justify-content: center;
                  margin: 0 auto; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);">
                <span style="color: white; font-size: 36px;">⚡</span>
            </div>
        </div>
        <h2 style="text-align: center; color: white; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);">BetterSave Energy</h2>
    """, unsafe_allow_html=True)

# Apply Background Image
try:
    add_bg_from_local("static/BK1.jpg")  # Path to the background image in static folder
except Exception as e:
    st.error(f"Error loading background: {e}")
    # Add a fallback dark background
    st.markdown("""
        <style>
        .stApp {
            background-color: #080f25;
        }
        </style>
    """, unsafe_allow_html=True)

# Add sidebar with simple navigation
with st.sidebar:
    # Logo
    render_logo()

    st.markdown("### Welcome to BetterSave")

    st.markdown("""
    Explore our energy dashboard to see how we're helping
    optimize renewable energy distribution across Germany.
    """)

    st.markdown("---")

    # Navigation section
    st.markdown("### Navigation")

    # Current page indicator
    st.markdown("**🏠 Home** (current page)")

    # Simple navigation using custom styled links
    st.markdown("""
    <div class="sidebar-navigation">
        <a href="/Pages/Dashboard" target="_self" class="sidebar-link">🔍 Dashboard</a>
        <a href="/Pages/Prediction" target="_self" class="sidebar-link">📊 Predictions</a>
        <a href="/Pages/About" target="_self" class="sidebar-link">ℹ️ About Us</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<div style='text-align: center; opacity: 0.7;'>BetterSave Energy Analytics Platform</div>", unsafe_allow_html=True)

# Main content area
st.markdown("<h1 style='margin-top: 20px; font-size: 3rem;'>BetterSave Energy</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.5rem;'>Intelligent Energy Storage and Distribution</p>", unsafe_allow_html=True)

# Add some spacing
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# State Variables for Video Playback
if "play_video" not in st.session_state:
    st.session_state.play_video = False

# "EXPLORE MORE" Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("EXPLORE MORE", key="explore", use_container_width=True):
        st.session_state.play_video = True  # Set session state to trigger video

# Render Video & Close Button
if st.session_state.play_video:
    try:
        st.video("static/Final_video.MP4")  # Path to the video file inside static folder
    except Exception as e:
        st.error(f"Error loading video: {e}")

    # Close Video Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("CLOSE VIDEO", key="close", use_container_width=True):
            st.session_state.play_video = False  # Stop playing the video
            st.rerun()  # Use the correct method to refresh the page

# Floating Email Button in Bottom-Right
st.markdown(
    '<a class="email-button" href="mailto:officialkhashayar@gmail.com">Write to Us</a>',
    unsafe_allow_html=True
)
