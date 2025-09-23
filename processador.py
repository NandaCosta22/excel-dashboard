import pandas as pd
import plotly.express as px


def gerar_grafico(caminho, tipo='bar'):
    df = pd.read_excel(caminho)
    print("Dados carregados:", df.head())  # 👈 Verifica se os dados foram lidos

    if tipo == 'line':
        fig = px.line(df, x=df.columns[0], y=df.columns[1])
    elif tipo == 'pie':
        fig = px.pie(df, names=df.columns[0], values=df.columns[1])
    else:
        fig = px.bar(df, x=df.columns[0], y=df.columns[1])

    html = fig.to_html(full_html=False)
    print("HTML do gráfico:", html[:200])  # 👈 Verifica se o gráfico foi gerado
    return html


