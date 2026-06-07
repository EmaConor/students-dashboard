import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

load_dotenv()

EXCEL_PATH = os.getenv("EXCEL_FILE_PATH", "ListadoDeEstudiantesGrupo_051.xlsx")
SHEET_NAME = os.getenv("SHEET_NAME", "Hoja2")

st.set_page_config(
    page_title="Dashboard Estudiantes Grupo 051",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

dfDatos = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

# Limpiar y preparar datos
dfDatos['Fecha_Nacimiento'] = pd.to_datetime(dfDatos['Fecha_Nacimiento'], errors='coerce')
dfDatos['Edad'] = (datetime.now() - dfDatos['Fecha_Nacimiento']).dt.days // 365

# Estandarizar Estatura a metros
def estandarizar_metros(valor):
    # Si el valor es NaN, devolverlo tal cual
    if pd.isna(valor):
        return valor
    
    # Si el valor está entre 100 y 250, está en cm -> convertir a m
    if 100 <= valor <= 250:
        return round(valor / 100, 2)
    # Si el valor está entre 1 y 3, ya está en metros
    elif 1 <= valor <= 3:
        return round(valor, 2)
    # Para cualquier otro caso, mantener el valor
    else:
        return valor

dfDatos['Estatura'] = pd.to_numeric(dfDatos['Estatura'], errors='coerce')
dfDatos['Estatura'] = dfDatos['Estatura'].apply(estandarizar_metros)
dfDatos['Peso'] = pd.to_numeric(dfDatos['Peso'], errors='coerce')
dfDatos['Talla_Zapato'] = pd.to_numeric(dfDatos['Talla_Zapato'], errors='coerce')
dfDatos['Color_Cabello'] = dfDatos['Color_Cabello'].str.strip().str.title() #strip(): elimina espacios y title(): pone en mayuscula la primera letra de cada palabra
dfDatos['Barrio_Residencia'] = dfDatos['Barrio_Residencia'].str.strip().str.title() # Estandarizar formato de barrio

# Calcular el indice de masa corporal
dfDatos['Indice_Masa_Corporal'] = round(dfDatos['Peso'] / ((dfDatos['Estatura']) ** 2), 2)

with st.sidebar:
    st.header("Filtros")
    parRH = st.multiselect('Tipo de Sangre (RH)', options=dfDatos['RH'].dropna().unique())
    parColorCabello = st.multiselect('Color de Cabello', options=dfDatos['Color_Cabello'].dropna().unique()) #dropna hace que no aparezca las opciónes None
    parBarrio = st.multiselect('Barrio de Residencia', options=dfDatos['Barrio_Residencia'].dropna().unique())
    
    min_edad, max_edad = st.slider('Rango de Edad', 
                                  min_value=int(dfDatos['Edad'].min()), 
                                  max_value=int(dfDatos['Edad'].max()),
                                  value=(int(dfDatos['Edad'].min()), int(dfDatos['Edad'].max())))
    
    min_estatura, max_estatura = st.slider('Rango de Estatura (cm)', 
                                          min_value=float(dfDatos['Estatura'].min()), 
                                          max_value=float(dfDatos['Estatura'].max()),
                                          value=(float(dfDatos['Estatura'].min()), float(dfDatos['Estatura'].max())))

# Aplicar filtros
dfFiltrado = dfDatos.copy()

if len(parRH) > 0:
    dfFiltrado = dfFiltrado[dfFiltrado['RH'].isin(parRH)]

if len(parColorCabello) > 0:
    dfFiltrado = dfFiltrado[dfFiltrado['Color_Cabello'].isin(parColorCabello)]

if len(parBarrio) > 0:
    dfFiltrado = dfFiltrado[dfFiltrado['Barrio_Residencia'].isin(parBarrio)]

dfFiltrado = dfFiltrado[(dfFiltrado['Edad'] >= min_edad) & 
                        (dfFiltrado['Edad'] <= max_edad) &
                        (dfFiltrado['Estatura'] >= min_estatura) & 
                        (dfFiltrado['Estatura'] <= max_estatura)
]

# Mostrar datos filtrados
st.dataframe(dfFiltrado)

st.header('Dashboard Estudiantil - Grupo 051')

# Métricas principales
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    total_estudiantes = len(dfFiltrado)
    st.metric("Total Estudiantes", f'{total_estudiantes}')
with c2:
    edad_promedio = dfFiltrado['Edad'].mean()
    st.metric("Edad Promedio", f'{edad_promedio:.2f} años')
with c3:
    estatura_promedio = dfFiltrado['Estatura'].mean()
    st.metric("Estatura Promedio", f'{estatura_promedio:.2f} cm')
with c4:
    peso_promedio = dfFiltrado['Peso'].mean()
    st.metric("Peso Promedio", f'{peso_promedio:.2f} kg')
with c5:
    imc_promedio = dfFiltrado['Indice_Masa_Corporal'].mean()
    st.metric("Indice_Masa_Corporal Promedio", f'{imc_promedio:.2f}')

# Primera fila de gráficos
c1, c2 = st.columns(2)
with c1:
    dfEdadDist = dfFiltrado['Edad'].value_counts().sort_index().reset_index()
    dfEdadDist.columns = ['Edad', 'Cantidad']
    fig = px.bar(dfEdadDist, x='Edad', y='Cantidad', title='Distribución por Edad')
    st.plotly_chart(fig, use_container_width=True)
with c2:
    dfRH = dfFiltrado['RH'].value_counts().reset_index()
    dfRH.columns = ['RH', 'Cantidad']
    fig = px.pie(dfRH, values='Cantidad', names='RH', title='Distribución por Tipo de Sangre')
    st.plotly_chart(fig, use_container_width=True)

# Segunda fila de gráficos
c1, c2 = st.columns(2)
with c1:
    fig = px.scatter(dfFiltrado, x='Estatura', y='Peso', color='RH', 
                    title='Relación Estatura vs Peso', hover_data=['Nombre_Estudiante'])
    st.plotly_chart(fig, use_container_width=True)
with c2:
    dfColorCabello = dfFiltrado['Color_Cabello'].value_counts().reset_index()
    dfColorCabello.columns = ['Color_Cabello', 'Cantidad']
    fig = px.bar(dfColorCabello, x='Color_Cabello', y='Cantidad', 
                title='Distribución por Color de Cabello', color='Color_Cabello')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# Tercera fila de gráficos
c1, c2 = st.columns(2)
with c1:
    dfTallaZapato = dfFiltrado.groupby('Talla_Zapato').size().reset_index()
    dfTallaZapato.columns = ['Talla_Zapato', 'Cantidad']
    fig = px.line(dfTallaZapato, x='Talla_Zapato', y='Cantidad', 
                 title='Distribución de Tallas de Zapato')
    st.plotly_chart(fig, use_container_width=True)
with c2:
    dfBarrios = dfFiltrado['Barrio_Residencia'].value_counts().head(10).reset_index()
    dfBarrios.columns = ['Barrio_Residencia', 'Cantidad']
    fig = px.bar(dfBarrios, x='Barrio_Residencia', y='Cantidad', 
                title='Top 10 Barrios de Residencia', color='Barrio_Residencia')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# Tablas top 5
c1, c2 = st.columns(2)
with c1:
    st.subheader('Top 5 - Mayor Estatura')
    dfTopEstatura = dfFiltrado.sort_values(by = 'Estatura', ascending=False).head(5)[['Nombre_Estudiante', 'Apellido_Estudiante', 'Estatura', 'Peso']]
    st.table(dfTopEstatura)
with c2:
    st.subheader('Top 5 - Mayor Peso')
    dfTopPeso = dfFiltrado.sort_values(by = 'Peso', ascending=False).head(5)[['Nombre_Estudiante', 'Apellido_Estudiante', 'Peso', 'Estatura']]
    st.table(dfTopPeso)

# Información general
st.subheader("Resumen Estadístico")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Estatura")
    st.write(f"Mínima: {dfFiltrado['Estatura'].min():.2f} cm")
    st.write(f"Máxima: {dfFiltrado['Estatura'].max():.2f} cm")
    st.write(f"Promedio: {dfFiltrado['Estatura'].mean():.2f} cm")
with col2:
    st.subheader("Peso")
    st.write(f"Mínimo: {dfFiltrado['Peso'].min():.2f} kg")
    st.write(f"Máximo: {dfFiltrado['Peso'].max():.2f} kg")
    st.write(f"Promedio: {dfFiltrado['Peso'].mean():.2f} kg")
with col3:
    st.subheader("Indice Masa Corporal")
    st.write(f"Mínimo: {dfFiltrado['Indice_Masa_Corporal'].min():.2f}")
    st.write(f"Máximo: {dfFiltrado['Indice_Masa_Corporal'].max():.2f}")
    st.write(f"Promedio: {dfFiltrado['Indice_Masa_Corporal'].mean():.2f}")

# python -m venv venv
# source venv/bin/activate (Linux/Mac) o venv\Scripts\activate (Windows)
# pip install streamlit plotly pandas openpyxl o pip install -r requirements.txt
#Para correrlo: streamlit run app.py
#Si no: python -m streamlit run app.py
#deactivate