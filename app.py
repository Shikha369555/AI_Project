import streamlit as st
st.set_page_config(page_title="AI Grievance System", page_icon="🤖", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 AI Grievance System</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>Enter your complaint and get the predicted department instantly.</p>",
    unsafe_allow_html=True
)
user_input = st.text_input("📝 Your Complaint", placeholder="e.g., Water leakage in my area")
if st.button("🔍 Predict Department"):
    st.success(f"✅ Predicted Department: {result[0]}")
st.markdown("---")
st.markdown("Made with ❤️ using AI")