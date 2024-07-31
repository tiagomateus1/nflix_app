import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actors_service = ActorService()
    actors = actors_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes')
        actors_df = pd.json_normalize(actors)

        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('Nenhum registro foi encontrado.')

    st.title('Cadastrar novo(a) Ator/Atriz')
    name = st.text_input('Nome do(a) Ator/Atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = ['BRA', 'USA', 'RUS', 'ARG']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    if st.button('Cadastrar'):
        new_actor = actors_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Ocorreu um erro ao cadastrar o(a) Ator/Atriz. Verifique os campos.')
