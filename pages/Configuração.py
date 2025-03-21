import streamlit as st
from configs import get_config

def config_page():
    st.header('Página de Configuração', divider=True)

    model_name = st.text_input('Modificar o modelo', value=get_config('model_name'))
    retrieval_search_type = st.text_input('Modificar o tipo de retrieval', value=get_config('retrieval_search_type'))
    retrieval_kwargs = st.text_input('Modificar os parâmetros de retrieval', value=get_config('retrieval_kwargs'))
    prompt = st.text_area('Modifique o prompt padrão:', height=350, value=get_config('prompt'))

    if st.button('Modificar parâmetros', use_container_width=True):
        st.session_state['model_name'] = model_name
        st.session_state['retrieval_search_type'] = retrieval_search_type
        st.session_state['retrieval_kwargs'] = retrieval_kwargs
        st.session_state['prompt'] = prompt

config_page()