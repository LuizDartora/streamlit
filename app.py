import numpy as np
import streamlit as st
import pandas as pd
import requests
import altair as alt
import fipe
import helper

api_url_referencia = "http://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia"
headers = {"Host": "veiculos.fipe.org.br", "Referer": "http://veiculos.fipe.org.br", "Content-Type": "application/json"}
response = requests.post(api_url_referencia, headers=headers)
lista_ref = response.json()

input_cod_fipe = st.text_input(
   "Digite o código fipe do veículo:",
   placeholder= "Formato 012345-9",
   max_chars=8
)
option_tipo = st.selectbox(
   "Selecione o tipo de veículo:",
   ("Carro", "Moto", "Caminhão"),
   index=None,
   placeholder="Escolha uma opção"
)
option_ano_modelo = st.selectbox(
   "Selecione o ano do modelo:",
   helper.get_anos_lista(),
   index=None,
   placeholder="Escolha uma opção"
)
option_combustivel = st.selectbox(
   "Selecione o tipo de combustível:",
   ("Diesel", "Gasolina"),
   index=None,
   placeholder="Escolha uma opção"
)
if option_ano_modelo != None:
    option_tempo_consulta = st.selectbox(
    "Selecione quantos meses de histórico gostaria de consultar:",
    helper.get_max_anos_consulta(option_ano_modelo),
    placeholder="Selecione o ano do modelo primeiro",
    )
ref = fipe.get_periodo_referencia()



if st.button('Consultar'):
    tipo = helper.get_tipo(option_tipo)
    lista_de_valores = fipe.get_valor_veiculo(ref,tipo,option_ano_modelo,input_cod_fipe,option_combustivel,option_tempo_consulta)
    df = pd.DataFrame(data = lista_de_valores, columns=["Data","Preço"])

    
    line = alt.Chart(df).mark_line().encode(
        alt.X('Data',sort=None, axis=alt.Axis(grid=True)),
        alt.Y('Preço', sort="descending", axis=alt.Axis(grid=True))        
    )
    points = alt.Chart(df).mark_point(size=200).encode(
        alt.X('Data',sort=None, axis=alt.Axis(grid=True)),
        alt.Y('Preço', sort="descending", axis=alt.Axis(grid=True))  
    )
    chart = line + points
    st.altair_chart(chart, use_container_width=True)

