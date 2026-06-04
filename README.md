# 🏠 Previsão de Preços de Imóveis Airbnb com Machine Learning

## 📖 Sobre o Projeto

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Concluído-green)

Este projeto foi desenvolvido com o objetivo de aplicar técnicas de Ciência de Dados e Machine Learning na previsão de preços de anúncios do Airbnb.

Durante o desenvolvimento foram realizadas etapas fundamentais do processo de análise de dados, incluindo:

* Coleta e consolidação dos dados;
* Limpeza e tratamento de valores nulos;
* Conversão e adequação de tipos de dados;
* Análise exploratória (EDA);
* Remoção de outliers;
* Engenharia de atributos;
* Codificação de variáveis categóricas;
* Treinamento e avaliação de modelos de Machine Learning;
* Exportação do modelo para utilização em aplicações futuras.

---

## 🎯 Objetivo

Construir um modelo capaz de prever o preço de uma hospedagem do Airbnb com base em características do imóvel, localização, avaliações e demais atributos presentes na base de dados.

---

## 🛠️ Tecnologias Utilizadas

### Linguagem

* Python

### Manipulação de Dados

* Pandas
* NumPy

### Visualização

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-Learn

  * Linear Regression
  * Random Forest Regressor
  * Extra Trees Regressor

### Persistência de Modelos

* Joblib

### Ambiente

* Jupyter Notebook

---

## 📂 Estrutura do Projeto

```text
projeto-ciencia-de-dados/
│
├── main.ipynb                  # Notebook principal
├── arquivo_deploy.py           # Arquivo para implantação do modelo
├── colunas.joblib             # Estrutura das features utilizadas
├── primeiros_registros.csv    # Amostra dos dados
├── primeiros_registros.xlsx   # Amostra dos dados para análise
├── requirements.txt           # Dependências do projeto
└── .gitignore
```

---

## 🔍 Etapas do Projeto

### 1. Importação e Consolidação dos Dados

Os arquivos da base de dados são carregados e consolidados em um único DataFrame para análise.

### 2. Limpeza dos Dados

Foram realizadas operações como:

* Remoção de colunas com excesso de valores nulos;
* Exclusão de registros incompletos;
* Conversão de tipos de dados;
* Padronização de valores monetários.

### 3. Análise Exploratória (EDA)

Foram utilizadas técnicas de visualização para compreender o comportamento dos dados:

* Heatmaps de correlação;
* Histogramas;
* Boxplots;
* Gráficos de distribuição;
* Visualização geográfica dos imóveis.

### 4. Tratamento de Outliers

Utilizando o método do Intervalo Interquartil (IQR), foram identificados e removidos valores extremos que poderiam prejudicar o treinamento dos modelos.

### 5. Engenharia de Atributos

Transformação e preparação das variáveis para uso em algoritmos de Machine Learning.

### 6. Treinamento dos Modelos

Foram avaliados diferentes algoritmos:

* Linear Regression
* Random Forest Regressor
* Extra Trees Regressor

### 7. Avaliação

Os modelos foram comparados utilizando métricas de regressão, permitindo identificar o melhor desempenho para previsão dos preços.

### 8. Exportação

O modelo final foi salvo utilizando Joblib para utilização posterior em aplicações web ou APIs.

---

## 🚀 Como Executar

### Clonar o repositório

```bash
git clone https://github.com/fernando-antonio-souza/projeto-ciencia-de-dados.git
```

### Entrar no diretório

```bash
cd projeto-ciencia-de-dados
```

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar o notebook

```bash
jupyter notebook
```

Abra o arquivo:

```text
main.ipynb
```

---

## 📈 Principais Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos importantes de Ciência de Dados:

* Manipulação de dados com Pandas;
* Visualização de dados;
* Tratamento de valores ausentes;
* Remoção de outliers;
* Correlação entre variáveis;
* Machine Learning supervisionado;
* Avaliação de modelos de regressão;
* Persistência de modelos treinados.

---

## 👨‍💻 Autor

Fernando Antonio Souza

GitHub: https://github.com/fernando-antonio-souza

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado em Ciência de Dados e Machine Learning.
