
import pandas as pd
import streamlit as st
import joblib

# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(page_title= "Previsão Airbnb", layout="centered")

st.title("🏠 Previsão de Preço Airbnb")



# CACHE (EVITA RECARREGAR TODA HORA)
@st.cache_resource
def carregar_modelo():
    return joblib.load("modelo.joblib")


@st.cache_resource
def carregar_colunas():
    return joblib.load("colunas.joblib")


modelo = carregar_modelo()
colunas_modelo = carregar_colunas()


# DICIONÁRIOS
x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'minimum_nights': 0,
                'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0 }

x_tf = { 'host_is_superhost': 0, 'instant_bookable': 0, 'is_location_exact': 0, 'is_business_travel_ready': 0 }

x_listas = {'property_type': [ 'Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': [ 'Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'bed_type': [ 'Real Bed', 'Outros'],
            'cancellation_policy': [ 'flexible', 'moderate', 'strict', 'strict_14_with_grace_period']}



# CRIAR DICIONÁRIO BASE
dicionario = {}

for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f"{item}_{valor}"] = 0



# INPUTS NUMÉRICOS
st.subheader("📌 Informações Numéricas")

for item in x_numericos:

    if item in ["latitude", "longitude"]:

        valor = st.number_input( item, step=0.00001, value=0.0,format="%.5f")

    elif item == "extra_people":

        valor = st.number_input( item, step=0.01, value=0.0)

    else:

        valor = st.number_input(item, step=1, value=0)

    x_numericos[item] = valor



# INPUTS TRUE/FALSE
st.subheader("✅ Características")

for item in x_tf:

    valor = st.selectbox(item, ("Sim", "Não"))

    if valor == "Sim":
        x_tf[item] = 1
    else:
        x_tf[item] = 0




# INPUTS CATEGÓRICOS
st.subheader("🏠 Tipos do Imóvel")

for item in x_listas:

    valor = st.selectbox(item, x_listas[item])

    dicionario[f"{item}_{valor}"] = 1




# BOTÃO
botao = st.button("Prever Valor do Imóvel")





# PREVISÃO
if botao:

    # junta tudo
    dicionario.update(x_numericos)
    dicionario.update(x_tf)

    # dataframe
    valores_x = pd.DataFrame(dicionario, index=[0])

    # adiciona colunas faltantes
    for coluna in colunas_modelo:

        if coluna not in valores_x.columns:
            valores_x[coluna] = 0

    # garante mesma ordem do treino
    valores_x = valores_x[colunas_modelo]

    # previsão
    preco = modelo.predict(valores_x)

    # resultado
    st.success(f"💰 Valor previsto: R$ {preco[0]:,.2f}")