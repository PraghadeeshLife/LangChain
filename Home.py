import streamlit as st

st.set_page_config(
    page_title="Speak to your Doc",
    page_icon="👋",
)

st.write("# Welcome to Speak to your Doc! 👋")

st.sidebar.success("Select Try to speak to your document.")

st.markdown(
    """
    Speak to your doc is a platform built on top of OpenAI API, that let's you to upload a PDF document and query any information related to the PDFs.

    **👈 Select Try from the sidebar** to play with Speak to your doc!
    ### 🚀 Built with
    - Python - StreamLit
    - LangChain
    - OpenAI
    ### 😮 Use Case
    - Have you been in a place where you take on a new project in a workplace, and struggle with understanding documentation and often end up in a confusion?
      With Speak to your doc, you could easily surf through your documentation and free yourself from confusions and equip yourself with clarity.
    ### 😑 TODOs
    - Implementation of Open Source LLMs
    - Support more than PDF File formats
    - Data Privacy
"""
)

