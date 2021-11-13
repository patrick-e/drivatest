import pandas as pd
import matplotlib.pyplot as plt

#leitura de csv
dados_empresa = pd.read_csv('DadosEmpresa.csv')
dados_endereco = pd.read_csv('DadosEndereco.csv')

#Filtro de empresa de opção simples
simples = dados_empresa[
        (dados_empresa["opcao_pelo_simples"] == "SIM")
    ]

#Filtragem de endereço
endereco = dados_empresa[
            (dados_endereco["municipio"] == "CURITIBA") |
            (dados_endereco["municipio"] == "LONDRINA")
        ]
#Filtro de capital
capital = endereco[
    (dados_empresa["capital_social"] > 5000)
]


#Separação de dados para a plotagem de gráfico
curitiba = dados_endereco[
    (dados_endereco["municipio"] == "CURITIBA")
    ]
curitiba = curitiba.groupby(["bairro"])
empresas_curitiba = curitiba.size().reset_index(name="quantidade")

#Geração de csv
simples.to_csv("OpcaoPeloSimples.csv")
capital.to_csv("FiltroEmpresa.csv")

#Plotagem de gráfico
plt.bar(empresas_curitiba["bairro"],empresas_curitiba["quantidade"])
plt.xticks(rotation=90,fontsize=7)
plt.ylabel("quantidade")
plt.xlabel("bairro")
plt.title("quantidade de empresas por bairros")
plt.show()