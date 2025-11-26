import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker - Taranpreet", page_icon="🔒")

st.title("🔒 Password Strength Checker")
st.caption("Built by Taranpreet Singh • Python Developer • AI & Cybersecurity")

password = st.text_input("Enter a password", type="password", help="Your password is never stored or logged")

if password:
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Make it at least 12 characters long")

    # Uppercase, lowercase, digits, symbols
    if re.search(r"[A-Z]", password): score += 20
    else: feedback.append("Add uppercase letters")
    if re.search(r"[a-z]", password): score += 10
    else: feedback.append("Add lowercase letters")
    if re.search(r"[0-9]", password): score += 20
    else: feedback.append("Add numbers")
    if re.search(r"[^A-Za-z0-9]", password): score += 25
    else: feedback.append("Add special characters (!@#$ etc.)")

    # Strength levels
    if score >= 90:
        strength, color = "Very Strong", "green"
    elif score >= 75:
        strength, color = "Strong", "lightgreen"
    elif score >= 60:
        strength, color = "Moderate", "orange"
    else:
        strength, color = "Weak", "red"

    st.markdown(f"### Strength: **<span style='color:{color}'>{strength}</span>**", unsafe_allow_html=True)
    st.progress(score / 100)

    if feedback:
        st.warning("Suggestions:\n" + "\n".join("• " + f for f in feedback))
    else:
        st.balloons()
        st.success("Perfect password! You're safe 🔐")

st.markdown("---")
st.markdown("Live projects: [ML Password API](https://ml-password-security-api.onrender.com) • [Secure Blog API](https://secure-blog-backend.onrender.com)")