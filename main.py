import streamlit as st
import login
import pandas as pd

login.generarLogin()

if "user" in st.session_state:
    st.subheader("Información")