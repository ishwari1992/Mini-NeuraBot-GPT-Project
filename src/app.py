import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Page Config (MUST be Streamlit command)
st.set_page_config(
    page_title="Mini NeuraBot-GPT",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# SIDEBAR
with st.sidebar:
    # Logo / App Name
    st.markdown(
        """
        <h2 style="text-align:center;">NeuraBot</h2>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Sidebar menu
    st.button("New Chat", use_container_width=True)
    st.button("Search Chats", use_container_width=True)
    st.button("Images", use_container_width=True)
    st.button("Apps", use_container_width=True)
    st.button("Projects", use_container_width=True)

    st.divider()

    st.caption("Powered by OpenAI-NeuraBot")

# MAIN CHAT UI
st.title("Mini NeuraBot-GPT")
st.write("Ask any question or generate content using AI")

user_input = st.text_area("Enter your question or prompt:", height=100)

def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content

if st.button("Generate Answer"):
    if user_input.strip():
        with st.spinner("AI is thinking..."):
            st.success(generate_response(user_input))
    else:
        st.warning("Please enter a prompt")