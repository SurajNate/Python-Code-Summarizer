import streamlit as st
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    AutoConfig,
    pipeline,
)
import subprocess
import pyperclip

# Ensure page configuration is set as the first Streamlit command
st.set_page_config(layout="wide")


def copy_to_clipboard(text):
    pyperclip.copy(text)

# Initialize the model, tokenizer, and pipeline
model_name = "sagard21/python-code-explainer"
tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = AutoConfig.from_pretrained(model_name)

# Set up the pipeline
pipe = pipeline("summarization", model=model, config=config, tokenizer=tokenizer)

# Streamlit UI
st.markdown("<h1 style='text-align: center;'>Python Code Summarizer 🐍</h1>", unsafe_allow_html=True)

st.markdown("---")

# Two columns for input and output
col1, col2 = st.columns(2)

with col1:
    st.session_state.raw_code = st.text_area(
        "Enter Python Code", height=350, value="def example():\n   print('Hello, World!')"
    )

with col2:
    st.subheader("Output")
    if "summary" in st.session_state:
        st.text_area("Summary", value=st.session_state.summary, height=400, disabled=False)
        # Button to copy the content
        if st.button("Copy", key="copy_button"):
            copy_to_clipboard(st.session_state.summary)
    

# Summarize button in a separate row
if st.button("Summarize Code", key="summarize_button", use_container_width=True):
    if 'raw_code' in st.session_state and st.session_state.raw_code.strip():
        raw_code = st.session_state.raw_code
        st.session_state.summary = pipe(raw_code)[0]["summary_text"]
    else:
        st.warning("Please enter some Python code to summarize.")

st.markdown("---")

# Data for the developers
developers = [
    {
        'name': 'Suraj Sunil Nate',
        'college': 'Rajiv Gandhi Institute of Technology, Mumbai',
        'department': 'Artificial Intelligence and Data Science',
        'roll_no': '733',
        'Course (Year)': 'B.E (Final Year)',
        'Email': 'surajnate29@gmail.com',
        'social_profiles': {
            'LinkedIn': 'https://www.linkedin.com/in/suraj-nate-50001a27b/',
            'GitHub': 'https://github.com/SurajNate',
            'YouTube': 'https://www.youtube.com/@suraj_nate',
            'Instagram': 'https://www.instagram.com/suraj_nate?igsh=aWdtbWVyb3FxNzR1'
        },
        'ratings': '🌟🌟🌟🌟🌟',
        'Contribution': 'Backend - UI - etc',
        'img': 'images/surajnate.gif',  # Path to Suraj's image
    },
    {
        'name': 'Om Ravindra Patil',
        'college': 'Rajiv Gandhi Institute of Technology, Mumbai',
        'department': 'Artificial Intelligence and Data Science',
        'roll_no': '764',
        'Course (Year)': 'B.E (Final Year)',
        'Email': 'ompatil9819@gmail.com',
        'social_profiles': {
            'LinkedIn': 'https://www.linkedin.com/in/om-patil-237ba7286?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app',
            'GitHub': 'https://github.com/johndoe',
            'Instagram': 'https://www.instagram.com/.om_patil._?igsh=MXNjbmlsbnBmNnZyOA=='
        },
        'ratings': '🌟🌟🌟🌟🌟',
        'Contribution': 'Backend - UI - etc',
        'img': 'images/ompatil.jpeg',  # Path to Om's image
    },
    {
        'name': 'Shreenidhi Danappa Medar',
        'college': 'Rajiv Gandhi Institute of Technology, Mumbai',
        'department': 'Artificial Intelligence and Data Science',
        'roll_no': '728',
        'Course (Year)': 'B.E (Final Year)',
        'Email': 'shreenidhi@gmail.com',
        'social_profiles': {
            'LinkedIn': 'https://www.linkedin.com/in/johndoe',
            'GitHub': 'https://github.com/johndoe',
            'Instagram': 'https://twitter.com/johndoe'
        },
        'ratings': '🌟🌟🌟🌟🌟',
        'Contribution': 'Backend - UI - etc',
        'img': 'images/shreenidhi.jpeg',  # Path to Shreenidhi's image
    },
]

def display_home():
    # Center the title using custom HTML
    st.markdown("<h1 style='text-align: center;'>Developer Team</h1>", unsafe_allow_html=True)
    st.header("Team Members")
    # Display a note about the button behavior
    st.write(
    "Click the button twice : "
    "The first click ends the current session, and the second click starts a new session."
    )
    for developer in developers:
        if st.button(developer['roll_no']+" - "+developer['name']+" "+developer['ratings'], use_container_width=False):
            st.session_state['current_profile'] = developer

def display_profile():
    developer = st.session_state['current_profile']
    st.title("Developer Profile")

    # Create two columns for image and details
    col1, col2 = st.columns([1, 1])  # Adjust the ratio as needed (1:2 ratio)

    with col1:
        # Display the profile image in the first column
        st.image(developer['img'], caption=developer['name'], use_container_width=True)

    with col2:
        # Display the details in the second column
        st.subheader("Details")
        st.write(f"**Name:** {developer['name']}")
        st.write(f"**Roll No:** {developer['roll_no']}")
        st.write(f"**Department:** {developer['department']}")
        st.write(f"**College:** {developer['college']}")
        st.write(f"**Course (Year):** {developer['Course (Year)']}")
        st.write(f"**Email:** {developer['Email']}")
        st.write(f"**Contribution:** {developer['Contribution']}")
        st.write(f"**Ratings:** {developer['ratings']}")

        st.subheader("Social Profiles")
        for platform, link in developer['social_profiles'].items():
            if platform == 'LinkedIn':
                icon = '🔗'
            elif platform == 'GitHub':
                icon = '🚀'
            elif platform == 'Instagram':
                icon = '📸'
            elif platform == 'YouTube':
                icon = '▶️'
            st.markdown(f"<a href='{link}' style='color: white; text-decoration: none; border: 1px solid white; padding: 5px;border-radius: 5px;'>{icon} {platform}</a>", unsafe_allow_html=True)


    
    if st.button("Back to Home", use_container_width=True):
        st.session_state['current_profile'] = None
    st.write(
    "Click the button twice : "
    "The first click ends the current session, and the second click starts a new session."
    )

# Initialize session state
if 'current_profile' not in st.session_state:
    st.session_state['current_profile'] = None

# Main rendering logic
if st.session_state['current_profile']:
    display_profile()
else:
    display_home()


# Display the GIF
# Path to your GIF
#gif_path = "path_to_your_gif.gif"
# Display the GIF
#st.image(gif_path, use_column_width=True)
