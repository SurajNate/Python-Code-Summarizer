import streamlit as st

# Dummy data for the developers
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
            'Instagram': 'https://www.instagram.com/suraj_nate?igsh=aWdtbWVyb3FxNzR1'
        },
        'ratings': '🌟🌟🌟🌟🌟',
        'Contribution': 'Backend - UI - etc',
        'img': 'images/surajnate.jpeg',  # Path to Suraj's image
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
    st.title("Developer Team")
    st.header("Team Members")
    for developer in developers:
        if st.button(developer['name']):
            st.session_state['current_profile'] = developer


def display_profile():
    developer = st.session_state['current_profile']
    st.title("Developer Profile")

    # Display the profile image at the top
    st.image(developer['img'], caption=developer['name'], width=600)  # Adjust the width to your preference

    # Display the details below the image
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
        st.markdown(f"<a href='{link}' style='color: white; text-decoration: none;'>{icon} {platform}</a>", unsafe_allow_html=True)

    if st.button("Back to Home"):
        st.session_state['current_profile'] = None


# Initialize session state
if 'current_profile' not in st.session_state:
    st.session_state['current_profile'] = None

# Main rendering logic
if st.session_state['current_profile']:
    display_profile()
else:
    display_home()
