# 📊 Excel Dashboard

Dashboard de Gráficos Interativos com Flask e Plotly — transforme planilhas Excel em visualizações dinâmicas com apenas alguns cliques.

---
## 🌐 Link do Projeto 

[Excel Dashboard](http://127.0.0.1:5000)

## 🚀 Tecnologias Utilizadas

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"></a>
  <a href="#"><img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"></a>
  <a href="#"><img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"></a>
  <a href="#"><img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"></a>
  <a href="#"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"></a>
</p>

---

## 🧠 Sobre o Projeto

Este projeto é uma aplicação web desenvolvida com **Flask** que permite ao usuário:

- Fazer upload de uma planilha `.xlsx` com até 4 colunas
- Escolher entre três tipos de gráfico: **barras**, **pizza** ou **linha**
- Visualizar o gráfico gerado com **Plotly**, diretamente na página
- Acompanhar uma animação de carregamento no botão, para melhor experiência

A interface é responsiva e moderna, com foco em usabilidade e visual limpo.

---

## 📁 Estrutura do Projeto

Estrutura/

├── app.py               # Arquivo principal Flask que roda o servidor

├── processador.py       # Função que processa os dados e gera os gráficos

├── templates/

│   └── index.html       # Página principal da aplicação

├── static/

│   ├── style.css        # Estilo visual da interface

│   └── script.js        # Animação do botão de carregamento

├── uploads/             # Pasta onde os arquivos Excel são salvos temporariamente

├── README.md            # Documentação do projeto


