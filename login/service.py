import streamlit as st
from api.service import Auth


def login(username, password):
    auth_service = Auth()
    responde = auth_service.get_token(
        username=username,
        password=password,
    )
    if responde.get('error'):
        st.error(f'Ocorreu um arro ao tentar realizar login: {responde.get("error")}')
    else:
        st.session_state.token = responde.get('access')
        st.rerun()


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
