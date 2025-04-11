import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker By Aqsa", page_icon="🌘", layout="centered")

st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;} 
    .stButton button {
        width: 50%;
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 18px;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Checker")
st.write("Check the strength of your password! 🔍")

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper and lower case
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1 
    else: 
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z)**.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")  

    # Display result
    if score == 4:
        st.success("✅ **Strong Password!** Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - consider adding more complexity.")
    else:
        st.error("❌ **Weak Password** - follow the suggestions below to strengthen it.")    

    # Feedback section
    if feedback:
        with st.expander("**Improve your password**"):
            for item in feedback:
                st.write(item)

# Password input
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong!")          

# Button
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first.")
