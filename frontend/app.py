import streamlit as st

import requests

st.title("Supervisor Agent System")

response = requests.get(
    "http://127.0.0.1:8000/stream",
    stream=True
)

placeholder = st.empty()

for line in response.iter_lines():

    if line:

        decoded = line.decode("utf-8")

        placeholder.write(decoded)