import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="Lab 6: Interactive Dashboard",
    page_icon="🚀",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    h1 {
        color: #00DBDE;
        background-image: linear-gradient(45deg, #00DBDE 0%, #FC00FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    .card {
        padding: 1.5rem;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)


st.title("Lab 6: Streamlit Playground")
st.markdown("Welcome to the interactive component showcase. Explore the various inputs below!")

with st.container():
    st.subheader("👤 User Profile")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("What's your name?", placeholder="Enter your name here...")
        age = st.slider("Select your age", 0, 100, 25)
    
    with col2:
        occupation = st.selectbox(
            "What is your occupation?",
            ("Student", "Engineer", "Data Scientist", "Designer", "Other")
        )
        birthday = st.date_input("When is your birthday?", datetime.date(2000, 1, 1))

st.divider()
st.subheader("⚙️ Preferences")

interests = st.multiselect(
    "What are your interests?",
    ["Machine Learning", "Deployment", "Frontend", "Backend", "Cloud Computing", "UI/UX"],
    default=["Machine Learning"]
)

is_subscribed = st.checkbox("Subscribe to our newsletter?")


st.divider()
if st.button("Generate Summary"):
    st.markdown("### 📝 Summary Card")
    
    summary_html = f"""
    <div class="card">
        <h4>User Details</h4>
        <p><strong>Name:</strong> {name if name else 'N/A'}</p>
        <p><strong>Age:</strong> {age}</p>
        <p><strong>Occupation:</strong> {occupation}</p>
        <p><strong>Birthday:</strong> {birthday}</p>
        <p><strong>Interests:</strong> {', '.join(interests)}</p>
        <p><strong>Subscribed:</strong> {'Yes' if is_subscribed else 'No'}</p>
    </div>
    """
    st.markdown(summary_html, unsafe_allow_html=True)
    
    st.markdown("#### 📊 Tabular Data View")
    user_data = {
        "Attribute": ["Name", "Age", "Occupation", "Birthday", "Interests", "Subscribed"],
        "Value": [
            str(name) if name else "N/A", 
            str(age), 
            str(occupation), 
            birthday.strftime("%Y-%m-%d"), 
            ", ".join(interests), 
            "Yes" if is_subscribed else "No"
        ]
    }
    df = pd.DataFrame(user_data)
    st.dataframe(df, width="stretch")
    
    st.balloons()
else:
    st.info("Fill out the information above and click 'Generate Summary' to see the magic!")

st.markdown("---")
st.caption("Lab 6 - Interactive Components Demo")
