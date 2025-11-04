from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from processador import gerar_grafico
from pathlib import Path
from typing import Optional
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        arquivo = request.files.get('arquivo')
        tipo: Optional[str] = request.form.get('tipo')  # tipo de gráfico (p.ex. 'bar','line','pie')

        if arquivo and arquivo.filename:
            uploads_dir = Path('uploads')
            uploads_dir.mkdir(parents=True, exist_ok=True)

            filename = secure_filename(arquivo.filename)
            caminho = uploads_dir / filename
            arquivo.save(str(caminho))

            # Passa o tipo para a função gerar_grafico
            grafico_html = gerar_grafico(str(caminho), tipo)
            return render_template('index.html', grafico=grafico_html)

    # Se for GET ou não tiver arquivo, renderiza a página normalmente
    return render_template('index.html', grafico=None)


if __name__ == '__main__':
    # Usa variável de ambiente PORT quando disponível (útil em deploy)
    port = int(os.environ.get('PORT', 5000))
    # Não chamamos app.run em nível de importação — só quando executado como script
    app.run(host='0.0.0.0', port=port, debug=True)
