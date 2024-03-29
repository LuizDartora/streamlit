import datetime
import pandas as pd
import altair as alt
import streamlit as st
import decimal

def get_ano():
    today = datetime.datetime.today()
    year = today.year
    return year

def get_mes():
    today = datetime.datetime.today()
    month = today.month
    return month

def get_anos_lista():
    today = datetime.datetime.today()
    year = today.year
    lista_anos = []
    for i in range(year,(year-60),-1):
        lista_anos.append(i)
    return lista_anos

def get_max_anos_consulta(ano_modelo):
    lista_months = []
    year = get_ano()
    if year == int(ano_modelo):
        months = (get_mes() + 4)
        for i in range(months,0,-1):
            lista_months.append(i)
        return reversed(lista_months)
    else:
        months = (year - int(ano_modelo)) * 12
        for i in range(months,0,-1):
            lista_months.append(i)
        return reversed(lista_months)
    
def get_tipo(tipo):
    if tipo == "Carro":
        return 1
    if tipo == "Moto":
        return 2
    if tipo == "Caminhão":
        return 3
    

def get_lista_marcas(lista_marcas):
    lista_marca = []
    for marca in lista_marcas:
        lista_marca.append(marca['Label'])
    # print(lista_marca)
    return lista_marca

def get_lista_modelos(lista_modelos,combustivel):
    lista_modelo = []
    try:
        for modelo in lista_modelos:
            # print(lista_modelos)
            lista_modelo.append(modelo['Label'])
        # print(lista_modelo)
        if combustivel == 3:
            # print(check_se_diesel(lista_modelo))
            return check_se_diesel(lista_modelo)
        if combustivel == 1:
            return lista_modelo
    except:
        print("Erro")
    

def lista_ano_combustivel(tipo):
    TEMPO = 70
    year = get_ano()
    year_stop = year - TEMPO
    gasolina = "Gasolina"
    diesel = "Diesel"
    ano_combustivel = []
    if tipo == 2:
        for i in range(year, year_stop, -1):
            ano_combustivel.append(str(i)+"-"+gasolina)
    else:
        for i in range(year, year_stop, -1):
            ano_combustivel.append(str(i)+"-"+gasolina)
            ano_combustivel.append(str(i)+"-"+diesel)
    return ano_combustivel

def get_ano_combustivel(ano_combustivel):
    combustivel = ano_combustivel[5:]
    ano = ano_combustivel[:4]
    if combustivel == "Gasolina":
        id_combustivel = 1
        completo = ano + '-' + str(id_combustivel)
    if combustivel == "Diesel":
        id_combustivel = 3
        completo = ano + '-' + str(id_combustivel)
    valor_ano_combustivel =[ano,id_combustivel,completo]
    return valor_ano_combustivel
            
def get_cod_marca(nome_marca,lista_marcas):
    for marca in lista_marcas:
        if nome_marca == marca['Label']:
            return marca['Value']
        
def get_cod_modelo(nome_modelo,lista_modelos):
    for modelo in lista_modelos:
        if nome_modelo == modelo['Label']:
            return modelo['Value']


def check_se_diesel(lista_modelos):
    nova_lista_modelos = []
    for modelo in lista_modelos:
        if "Diesel" in modelo:
            nova_lista_modelos.append(modelo)
        if "Dies." in modelo:
            nova_lista_modelos.append(modelo)
    return nova_lista_modelos

def make_graph(df, min_value, max_value):
    chart = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill="white", size=100), size=5).encode(
        alt.X('Data',sort=None, axis=alt.Axis(grid=True)),
        alt.Y('Valor Numerico:Q', sort="ascending", axis=alt.Axis(grid=True,format='$,.2f'), title="FIPE", scale=alt.Scale(domain=[min_value-(min_value * 0.01), max_value+(max_value * 0.01)]))
    ).interactive()
    return st.altair_chart(chart, use_container_width=True)
    
    



def data_frame_graph(lista_de_valores):
    # df = pd.DataFrame(data = lista_de_valores, columns=["Data","Preço"])
    # df['Valor Numerico'] = df['Preço'].replace(r'[^\d,]', '', regex=True).str.replace(',', '.').astype(float)
    min_valor = lista_de_valores['Valor Numerico'].min()
    max_valor = lista_de_valores['Valor Numerico'].max()

    return min_valor,max_valor

def data_frame_min_max(lista_de_valores):
    # df = pd.DataFrame(data = lista_de_valores, columns=["Data","Preço"])
    # df['Valor Numerico'] = df['Preço'].replace(r'[^\d,]', '', regex=True).str.replace(',', '.').astype(float)
    min = lista_de_valores['Valor Numerico'].idxmin()
    max = lista_de_valores['Valor Numerico'].idxmax()
    # print(min)
    # print(max)
    cols = ["Data","Fipe"]
    rows = [
        "Preço mínimo",
        "Preço máximo",
        ]
    data = [
        ([lista_de_valores['Data'][min]],[lista_de_valores['Preço'][min]]),
        ([lista_de_valores['Data'][max]],[lista_de_valores['Preço'][max]])]
    new_df = pd.DataFrame(data,columns=cols, index=rows)
    
    return new_df

def media(lista_de_valores):
    # df = pd.DataFrame(data = lista_de_valores, columns=["Data","Preço"])
    # df['Valor Numerico'] = df['Preço'].replace(r'[^\d,]', '', regex=True).str.replace(',', '.').astype(float)
    media = round(lista_de_valores['Valor Numerico'].mean(),2)
    media = decimal.Decimal(media).quantize(decimal.Decimal("0.00"))

    #     centavos = str(media)[len(str(media))-2:]
    #     centenas = str(media)[len(str(media))-6:len(str(media))-3]
    #     milhares = str(media)[len(str(media))-9:len(str(media))-6]
    #     milhoes = str(media)[:len(str(media))-7]

    return moeda(media)


def moeda(valor):
    centavos = str(valor)[len(str(valor))-2:]
    novo_media = str(int(valor))

    ponto = 1
    letra2 = ""
    controle = 1

    for letra in novo_media[::-1]:
        letra2+=str(letra)
        if ponto == 3 and controle < len(novo_media):
            letra2 = letra2 + "."
            ponto = 0
        controle+=1
        ponto += 1
        # count+=1
    letra23 =""
    for letra in letra2[::-1]:
        letra23+=str(letra)
    formatado = "R$ "+letra23+","+centavos
    return formatado

def make_data_frame(lista_de_valores):
    # print("Chegou aqui")
    df = pd.DataFrame(data = lista_de_valores, columns=["Data","Preço"])
    df['Valor Numerico'] = df['Preço'].replace(r'[^\d,]', '', regex=True).str.replace(',', '.').astype(float)
    return df


lista_historico = []
# @st.cache_data(show_spinner=False)
def add_historico(historico):
    if historico not in lista_historico:
        if len(lista_historico) < 50:
            lista_historico.insert(0,historico)
        else:
            lista_historico.pop()
            lista_historico.insert(0,historico)
    # print(lista_historico)
# @st.cache_data(show_spinner=False)
def get_historico():
    return lista_historico