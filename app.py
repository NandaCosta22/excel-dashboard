from flask import Flask, request, render_template
from processador import gerar_grafico
import os

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        arquivo = request.files['arquivo']
        tipo = request.form.get('tipo')  # 👈 Aqui você captura o tipo de gráfico

        if arquivo:
            os.makedirs('uploads', exist_ok=True)  # ✅ Garante que a pasta existe
            caminho = os.path.join('uploads', arquivo.filename)
            arquivo.save(caminho)


            # 👇 Passa o tipo para a função gerar_grafico
            grafico_html = gerar_grafico(caminho, tipo)
            return render_template('index.html', grafico=grafico_html)

    # 👇 Se for GET ou não tiver arquivo, renderiza a página normalmente
    return render_template('index.html', grafico=None)

if __name__ == '__main__':
    app.run(debug=True)
