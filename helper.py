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
    if year == ano_modelo:
        months = (get_mes() + 4)
        for i in range(months,0,-1):
            lista_months.append(i)
        return lista_months
    else:
        months = (year - ano_modelo) * 12
        for i in range(months,0,-1):
            lista_months.append(i)
        return lista_months
    
def get_tipo(tipo):
    if tipo == "Carro":
        return 1
    if tipo == "Moto":
        return 2
    if tipo == "Caminhão":
        return 3
    
