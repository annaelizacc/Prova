#Existe o arquivo app.py.

import streamlit as st          
import pandas as pd             
import plotly.express as px
import openpyxl

# No app.py, carregue acidentes.csv com pandas.    FEITO
st.set_page_config(page_title="Acidentes - Belo Horizonte", layout="wide")


@st.cache_data
def carregar_dados(caminho_arquivo):
    # Carrega todas as abas do Excel
    xls = pd.ExcelFile(caminho_arquivo)

    # Lê acidentes.csv no código FEITO
    df = pd.read_excel(caminho_arquivo)


    #ja me buguei 
    #df_filtrado = df[(df["NOMEUP"].isin(["Minas Gerais", "Rio de Janeiro"])) ].copy()
    #df_tabela = df_filtrado[["Minas Gerais", "Rio de Janeiro"]]

    #Faça um groupby pela coluna dia_semana. O groupby junta todos os acidentes do mesmo dia da semana
    #acho que o correto seria df.groupby('dia_semana')['domingo']   poremnão estou achando outro exemplo de groupby para me baser nele
    segunda = df.groupby('dia_semana')['segunda']
    terca = df.groupby('dia_semana')['terca']
    quarta = df.groupby('dia_semana')['quarta']
    quinta = df.groupby('dia_semana')['quinta']
    sexta = df.groupby('dia_semana')['sexta']
    sabado = df.groupby('dia_semana')['sabado']
    domingo = df.groupby('dia_semana')['domingo']

    
    pop_semana = (
        df.groupby('segunda')['quantidade_pessoas']
        .sum()
        .reset_index()
        )
    pop_semana = (
        df.groupby('terca')['quantidade_pessoas']
        .sum()
        .reset_index()
        )
    
    pop_semana = (
        df.groupby('quarta')['quantidade_pessoas']
        .sum()
        .reset_index()
        )
    
    pop_semana = (
        df.groupby('quinta')['quantidade_pessoas']
        .sum()
        .reset_index()
        )
    
    pop_semana = (
        df.groupby('sexta')['quantidade_pessoas']
        .sum()
        .reset_index()
        )
    
    pop_semana = (
        df.groupby('sabado')['quantidade_pessoas']
        .sum()
        .reset_index()
        )

    pop_semana = (
        df.groupby('domingo')['quantidade_pessoas']
        .sum()
        .reset_index()
        )   
    # Calcule a soma total de acidentes de cada dia. Como cada registro é um acidente, esse total é a
    #quantidade de registros do grupo. Não some quantidade_mortos, quantidade_feridos,
    #quantidade_pessoas nem quantidade_veiculos

       
    
    #TENHA MISERICORDIA DE MIM PROFESSORA 

df_filtrado = df[(df["NOMEUP"].isin(["Minas Gerais", "Rio de Janeiro"])) ].copy()
df_tabela = df_filtrado[["Minas Gerais", "Rio de Janeiro"]]
# Carregar arquivo
caminho_arquivo = r"H:\Python\ProvaFinalPython\acidentes.xlsx"




# st.title com o título do painel.
st.title("Painel Streamlit  Acidentes do Brasil")

# st.header com um cabeçalho da seção exibida
st.sidebar.header("Acidentes")

# Barra lateral (st.sidebar) com um controle que troca a visualização entre Tabela e Gráfico
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])


if opcao == "Tabela":
   
    st.header("Tabela do Acidentes ")
    #aqui tem que conter o dia da semana com a soma total dos acidentes
    st.dataframe(df_tabela , use_container_width=True, hide_index=True)
    
elif opcao == "Gráficos":
    st.header("Gráficos da semana")

    #achar a linha de barras

    st.subheader(" Gráfico de Barras")

    #NÃO DEU TEMPO DE MUDAR NADA DENTRO DO GRAFICO 
    fig_barras = px.bar(
        df_tabela,
        x="ANO",
        y="IQVU",
        color="NOMEUP",
        barmode="group",
        title="Comparativo Anual de IQVU (Barras Agrupadas)",
        color_discrete_map={"Taquaril": "#FF6B6B", "Santa Ines": "#00F5D4"},
        template="plotly_dark"
    )
    fig_barras.update_xaxes(type="category")  # só os anos existentes no eixo X
    st.plotly_chart(fig_barras, use_container_width=True)

    

    #exemplo de grafico de barras empilhdas da atividade de python e matematica
   # fig_empilhado = px.bar(
    #     dados_empilhado,
    #    x="Bairro",
    #    y="Valor",
    #    color="Dimensao",
    #    barmode="stack",
    #    title="Composição do IQVU por Dimensão — Ano 2016 (Barras Empilhadas)",
    #    template="plotly_dark"
    #)
    #st.plotly_chart(fig_empilhado, use_container_width=True)















#A fonte https://basedosdados.org/ aparece no painel.  FEITO
st.markdown("---")
st.caption("Fonte dos dados: dados abertos da Prefeitura de Belo Horizonte — https://basedosdados.org/")