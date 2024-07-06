import streamlit as st
import pandas as pd

def generarMenu(user):
    "Pagina 1"
    with st.sidebar:
        bttn = st.button("Salir")
        if bttn:
            st.session_state.clear()
            st.rerun()

def validarUsuario(usuario, password):
    df_users = pd.read_csv("users.csv", dtype=str)
    f1 = df_users[df_users["user"]==usuario]
    f2 = f1[f1["clave"] == password]
    if len(f2) > 0:
        return True
    else:
        return False



def generarLogin():
    if "user" in st.session_state:
        #generarMenu(st.session_state["user"])
        pass
    else:
        with st.form("frmLogin"):
            st.header("INICIO DE SESIÓN")
            user = st.text_input("User")
            password = st.text_input("Password", type="password")
            bttn = st.form_submit_button("Ingresar")
            if bttn:
                if validarUsuario(user, password):
                    st.session_state["user"] = user
                    st.rerun()
                else:
                    st.error("Incorrect user or password")
                