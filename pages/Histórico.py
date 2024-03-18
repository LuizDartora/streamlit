import streamlit as st
import helper

st.header("Histórico de Consultas", anchor=False)

lista_historico = helper.get_historico()
for n in range(len(lista_historico)):
    with st.expander(lista_historico[n]['modelo']+" "+lista_historico[n]['tempo'] +" "+ str(lista_historico[n]['historico']) +" Meses"):
        st.subheader(lista_historico[n]['marca'],divider="red", anchor=False)
        st.header(lista_historico[n]['modelo'], anchor=False)
        st.write(lista_historico[n]['tempo'])
        st.markdown(lista_historico[n]['fipe'])
        st.write(lista_historico[n]['medio'])

        st.write(lista_historico[n]['min_max'])

        helper.make_graph(lista_historico[n]['lista_valor'],lista_historico[n]['min'],lista_historico[n]['max'])
