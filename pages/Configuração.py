import json

import streamlit as st

from configs import get_config
from utils import PASTA_ARQUIVOS, cria_chain_conversa

def config_page():
    st.header('Página de configuração', divider=True)

    model_name = st.text_input('Modifique o modelo', value=get_config('model_name'))
    retrieval_search_type = st.text_input('Modifique o tipo de retrieval', value=get_config('retrieval_search_type'))
    retrieval_kwargs = st.text_input('Modifique os parâmetros de retrieval', value=json.dumps(get_config('retrieval_kwargs')))
    prompt = st.text_area('Modifique o prompt padrão', height=350, value=get_config('prompt'))


    if st.button('Salvar parâmetros', use_container_width=True):
        try:
            retrieval_kwargs = json.loads(retrieval_kwargs.replace("'", '"'))
            st.session_state['model_name'] = model_name
            st.session_state['retrieval_search_type'] = retrieval_search_type
            st.session_state['retrieval_kwargs'] = retrieval_kwargs
            st.session_state['prompt'] = prompt
            st.rerun()
        except json.JSONDecodeError:
            st.error("Erro ao salvar parâmetros: formato inválido. Certifique-se de que está no formato JSON correto.")
    
    if st.button('Atualizar ChatBot', use_container_width=True):
        if len(list(PASTA_ARQUIVOS.glob('*.pdf'))) == 0:
            st.error('Adicione arquivos .pdf para inicializar o chatbot')
        else:
            st.success('Inicializando o ChatBot...')
            cria_chain_conversa()
            st.rerun()


config_page()