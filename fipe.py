import requests

headers = {"Host": "veiculos.fipe.org.br", "Referer": "http://veiculos.fipe.org.br", "Content-Type": "application/json"}
api_url_completa = "http://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros"
api_url_referencia = "http://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia"

def get_periodo_referencia():
    response = requests.post(api_url_referencia, headers=headers)
    lista_ref = response.json()
    return lista_ref

def get_tempo():
    ...

def get_valor_veiculo(periodo_referencia, tipo, ano_modelo, cod_fipe, combustivel,tempo):
    listaPreco=[]
    for i in range(tempo, -1, -1):
        body = {
        "codigoTabelaReferencia": periodo_referencia[i]['Codigo'],
        "codigoTipoVeiculo": tipo,
        "anoModelo": ano_modelo,
        "modeloCodigoExterno": cod_fipe,
        "codigoTipoCombustivel": combustivel,
        "tipoConsulta": "codigo"
        }
        response = requests.post(api_url_completa,headers=headers, json=body)
        lista_fipe = response.json()
        # print(lista_fipe)
        tablePreco = {
                'Preço': lista_fipe['Valor'],
                'Data': periodo_referencia[i]['Mes']
            }
        listaPreco.append(tablePreco)
    return listaPreco