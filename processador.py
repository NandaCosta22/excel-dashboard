import pandas as pd
import plotly.express as px

def gerar_grafico(caminho, tipo='bar'):
    df = pd.read_excel(caminho)
    print("Dados carregados:", df.head())

    # Verifica se a planilha tem entre 2 e 4 colunas
    if df.shape[1] < 2 or df.shape[1] > 4:
        return "<p style='color:red;'>Erro: A planilha deve conter entre 2 e 4 colunas.</p>"

    # Gera um único gráfico com base no tipo escolhido
    if tipo == 'line':
        fig = px.line(df, x=df.columns[0], y=df.columns[1:])
    elif tipo == 'pie':
        # Pie só funciona com uma coluna de valores, então usamos a segunda
        fig = px.pie(df, names=df.columns[0], values=df.columns[1])
    else:  # 'bar'
        fig = px.bar(df, x=df.columns[0], y=df.columns[1:], barmode='group')

    html = fig.to_html(full_html=False)
    print("HTML do gráfico:", html[:200])
    return html



