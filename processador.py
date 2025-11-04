import pandas as pd
import plotly.express as px
from typing import Optional


def gerar_grafico(caminho: str, tipo: Optional[str] = 'bar') -> str:
    """Lê um arquivo Excel em 'caminho' e retorna o HTML do gráfico gerado.

    Em caso de erro retorna uma mensagem HTML com estilo vermelho.
    """
    try:
        df = pd.read_excel(caminho)
    except Exception as e:
        return f"<p style='color:red;'>Erro ao ler o arquivo: {e}</p>"

    # Verifica se a planilha tem entre 2 e 4 colunas
    if df.shape[1] < 2 or df.shape[1] > 4:
        return "<p style='color:red;'>Erro: A planilha deve conter entre 2 e 4 colunas.</p>"

    # Gera um único gráfico com base no tipo escolhido
    try:
        if tipo == 'line':
            fig = px.line(df, x=df.columns[0], y=df.columns[1:])
        elif tipo == 'pie':
            # Pie só funciona com uma coluna de valores, então usamos a segunda
            fig = px.pie(df, names=df.columns[0], values=df.columns[1])
        else:  # 'bar' por padrão
            fig = px.bar(df, x=df.columns[0], y=df.columns[1:], barmode='group')

        html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return html
    except Exception as e:
        return f"<p style='color:red;'>Erro ao gerar o gráfico: {e}</p>"



