import streamlit as st

# Page configuration
st.set_page_config(page_title="Homepage", layout="wide")

# --- LIGHT BLUE GRADIENT BACKGROUND + STYLING ---
st.markdown("""
    <style>
        /* Full-page light blue gradient */
        .stApp {
            background: linear-gradient(to right, #e0f7fa, #b3e5fc);
            background-attachment: fixed;
            color: #01579b;
        }

        .title {
            font-family: "Poppins", sans-serif;
            font-size: 48px;
            font-weight: 700;
            color: #0277bd;
            text-align: center;
            margin-top: 30px;
        }

        .subtitle {
            font-family: "Poppins", sans-serif;
            font-size: 24px;
            text-align: center;
            margin-bottom: 40px;
        }

        .stButton>button {
            font-family: "Poppins", sans-serif;
            font-size: 18px;
            padding: 12px 24px;
            width: 100%;
            background-color: #4fc3f7;
            color: white;
            border: none;
            border-radius: 10px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.15);
        }

        .stButton>button:hover {
            font-family: "Poppins", sans-serif;
            background-color: #29b6f6;
            color: white;
            transform: scale(1.03);
            transition: 0.2s;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="title">AQI Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Select a place to view predicted air quality levels</div>', unsafe_allow_html=True)

# --- LOCATION BUTTONS ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button(" Karyavattom"):
        st.switch_page("pages/karyavattom.py")

with col2:
    if st.button(" Kollam"):
        st.switch_page("pages/kollam.py")

with col3:
    if st.button(" Eloor"):
        st.switch_page("pages/eloor.py")