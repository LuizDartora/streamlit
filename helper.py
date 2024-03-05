import datetime

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
    for modelo in lista_modelos:
        lista_modelo.append(modelo['Label'])
    # print(lista_modelo)
    if combustivel == 3:
        # print(check_se_diesel(lista_modelo))
        return check_se_diesel(lista_modelo)
    if combustivel == 1:
        return lista_modelo 

def lista_ano_combustivel():
    TEMPO = 70
    year = get_ano()
    year_stop = year - TEMPO
    gasolina = "Gasolina"
    diesel = "Diesel"
    ano_combustivel = []
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

