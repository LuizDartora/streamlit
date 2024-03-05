import streamlit as st
import pandas as pd
import altair as alt
import fipe
import helper

#  Antigo por codigo
# input_cod_fipe = st.text_input(
#    "Digite o código fipe do veículo:",
#    placeholder= "Formato 012345-9",
#    max_chars=8
# )
# option_tipo = st.selectbox(
#    "Selecione o tipo de veículo:",
#    ("Carro", "Moto", "Caminhão"),
#    index=None,
#    placeholder="Escolha uma opção"
# )
# option_ano_modelo = st.selectbox(
#    "Selecione o ano do modelo:",
#    helper.get_anos_lista(),
#    index=None,
#    placeholder="Escolha uma opção"
# )
# option_combustivel = st.selectbox(
#    "Selecione o tipo de combustível:",
#    ("Diesel", "Gasolina"),
#    index=None,
#    placeholder="Escolha uma opção"
# )
# if option_ano_modelo != None:
#     option_tempo_consulta = st.selectbox(
#     "Selecione quantos meses de histórico gostaria de consultar:",
#     helper.get_max_anos_consulta(option_ano_modelo),
#     placeholder="Selecione o ano do modelo primeiro",
#     )
# ref = fipe.get_periodo_referencia()
#Fim antigo por codigo

# NOVO
ref = fipe.get_periodo_referencia()
option_tipo = st.selectbox(
   "Selecione o tipo de veículo:",
   ("Carro", "Moto", "Caminhão"),
   index=None,
   placeholder="Escolha uma opção"
)
if option_tipo != None:
   tipo = helper.get_tipo(option_tipo)
   lista_marcas = fipe.get_marcas(ref,tipo)
   marca = helper.get_lista_marcas(lista_marcas)
   option_marca = st.selectbox(
      "Selecione a marca do veículo:",
      marca,
      index=None,
      placeholder="Escolha uma opção"
   )
   

# if option_marca != None:
option_tempo = st.selectbox(
"Selecione o ano do modelo:",
helper.lista_ano_combustivel(),
index=None,
placeholder="Escolha uma opção", disabled=False
)

if(option_tempo != None):
   ano,combustivel,ano_combustivel = helper.get_ano_combustivel(option_tempo)
   cod_marca = helper.get_cod_marca(option_marca,lista_marcas)
   lista_modelos,comb = fipe.get_marcas_modelo(ref, tipo, ano, ano_combustivel, cod_marca, combustivel)
   modelos = helper.get_lista_modelos(lista_modelos,comb)
   option_modelo = st.selectbox(
   "Selecione o modelo:",
   modelos,
   index=None,
   placeholder="Escolha uma opção", disabled=False
   )

   option_historico = st.selectbox(
   "Selecione o tempo do histórico:",
   helper.get_max_anos_consulta(ano),
   index=None,
   placeholder="Escolha uma opção", disabled=False
   )
# periodo_referencia, tipo, cod_marca, ano_combustivel, ano_modelo, cod_modelo, combustivel,tempo
if st.button('Consultar'):
    tipo = helper.get_tipo(option_tipo)
   #  print(option_modelo)
   #  print(lista_modelos)
    cod_modelo = helper.get_cod_modelo(option_modelo,lista_modelos)
    st.write(option_modelo)
   #  st.write("A consulta está sendo feita com os seguintes dados "  +" "+str(tipo) +" "+str(cod_marca) +" "+str(ano_combustivel) +" "+str(ano) +" "+str(cod_modelo) +" "+str(combustivel))
    lista_de_valores = fipe.get_valor_veiculo_modelo(ref,tipo,cod_marca, ano_combustivel, ano, cod_modelo, combustivel,option_historico)
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

# FIM NOVO



# if st.button('Consultar'):
#     tipo = helper.get_tipo(option_tipo)
#     lista_de_valores = fipe.get_valor_veiculo(ref,tipo,option_ano_modelo,input_cod_fipe,option_combustivel,option_tempo_consulta)
#     df = pd.DataFrame(data = lista_de_valores, columns=["Data","Preço"])

    
#     line = alt.Chart(df).mark_line().encode(
#         alt.X('Data',sort=None, axis=alt.Axis(grid=True)),
#         alt.Y('Preço', sort="descending", axis=alt.Axis(grid=True))        
#     )
#     points = alt.Chart(df).mark_point(size=200).encode(
#         alt.X('Data',sort=None, axis=alt.Axis(grid=True)),
#         alt.Y('Preço', sort="descending", axis=alt.Axis(grid=True))  
#     )
#     chart = line + points
#     st.altair_chart(chart, use_container_width=True)

