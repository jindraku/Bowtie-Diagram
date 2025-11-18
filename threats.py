import streamlit as st

st.markdown("""
<style>
.node-box {
    width: 220px;
    padding: 18px;
    margin: 12px auto;
    text-align: center;
    border-radius: 12px;
    font-weight: 600;
    border: 1px solid #b8a600;
    background: linear-gradient(to bottom, #fff8b0, #ffd800);
    box-shadow: 0px 0px 4px rgba(0,0,0,0.2);
    font-family: Arial, sans-serif;
}
</style>
""", unsafe_allow_html=True)

threats = [
    "Poor road conditions",
    "Driver fatigue or distraction",
    "Mechanical issues",
    "Improper cargo loading"
]

for t in threats:
    st.markdown(f"<div class='node-box'>{t}</div>", unsafe_allow_html=True)
