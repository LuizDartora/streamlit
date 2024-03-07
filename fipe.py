import requests
import helper
headers = {"Host": "veiculos.fipe.org.br", "Referer": "http://veiculos.fipe.org.br", "Content-Type": "application/json"}
api_url_completa = "http://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros"
api_url_referencia = "http://veiculos.fipe.org.br/api/veiculos/ConsultarTabelaDeReferencia"
api_url = "http://veiculos.fipe.org.br/api/veiculos/"

def get_periodo_referencia():
    response = requests.post(api_url_referencia, headers=headers)
    lista_ref = response.json()
    return lista_ref

def get_marcas_modelo(periodo_referencia, tipo, ano_modelo, ano_combustivel, cod_marca, combustivel):
    api_url_modelo = api_url + "ConsultarModelosAtravesDoAno"
    body = {
    "codigoTabelaReferencia": periodo_referencia[0]['Codigo'],
    "codigoTipoVeiculo": tipo,
    "codigoMarca": cod_marca,
    "ano": ano_combustivel,
    "codigoTipoCombustivel": combustivel,
    "anoModelo": ano_modelo
    }
    response = requests.post(api_url_modelo,headers=headers, json=body)
    lista_modelos = response.json()
    # print(lista_modelos)
    
    return lista_modelos,combustivel
    


def get_marcas(periodo_referencia,tipo):
    api_url_marcas = api_url + "ConsultarMarcas"
    # print(api_url_marcas)
    # print(periodo_referencia[0]['Codigo'])
    # print(tipo)
    body = {
        "codigoTabelaReferencia": periodo_referencia[0]['Codigo'],
        "codigoTipoVeiculo": tipo
    }
    response = requests.post(api_url_marcas, headers=headers, json=body)
    marcas = response.json()
    # print(marcas)
    return marcas

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


def get_valor_veiculo_modelo(periodo_referencia, tipo, cod_marca, ano_combustivel, ano_modelo, cod_modelo, combustivel,tempo):
    api_url_valor_modelo = api_url + "ConsultarValorComTodosParametros"
    listaPreco=[]
    for i in range(tempo, -1, -1):
        try:
            body = {
            "codigoTabelaReferencia": periodo_referencia[i]['Codigo'],
            "codigoTipoVeiculo": tipo,
            "codigoMarca": cod_marca,
            "ano": ano_combustivel,
            "codigoTipoCombustivel": combustivel,
            "anoModelo": ano_modelo,
            "codigoModelo": cod_modelo,
            "tipoConsulta": "tradicional"
            }

            response = requests.post(api_url_valor_modelo,headers=headers, json=body)
            lista_fipe = response.json()
            # print(lista_fipe)
            # print(body)
            
            tablePreco = {
                    'Preço': lista_fipe['Valor'],
                    'Data': periodo_referencia[i]['Mes']
                }
            listaPreco.append(tablePreco)
        except:
            print("teste")
    # print("Os valores recebidos sao " + str(tipo) +" " + str(cod_marca) +" " + str(ano_combustivel) +" " +str(ano_modelo) +" " +str(cod_modelo) +" " +str(combustivel) +" " )
    return listaPreco