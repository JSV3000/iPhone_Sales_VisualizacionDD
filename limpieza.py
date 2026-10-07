import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# CONFIGURACION VISUAL DE STREAMLIT
st.set_page_config(
    page_title="Ventas de iPhone 2025",
    page_icon="📱",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1 {
        text-align: left;
        font-size: 40px;
        margin-bottom: 10px;
        font-weight: 700;
        color: #FAFAFA !important;
    }

    h2 {
        text-align: left;
        margin-top: 30px;
        color: #FAFAFA !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("Ventas de iPhone 2025")

df = pd.read_csv('iphone_sales_data.csv')
print(df.head())

# INFORMACION
print(df.isnull().sum()) #Nos muestra la cantidad de valores nulos por columna

# LIMPIEZA
df = df.dropna() #Elimina los valores nulos
ventas_totales = df.groupby('iPhone_Model')['Quantity'].sum().reset_index()

print(ventas_totales)

df['Sale_Date'] = pd.to_datetime(df['Sale_Date']) # Corrección: Se cambió 'Data_sale' por 'Sale_Date'

ventas_tiempo = df.groupby(
    df['Sale_Date'].dt.to_period('M')
)['Quantity'].sum().reset_index() #Agrupa por mes y suma la cantidad de ventas


# GRAFICA DE BARRAS (MATPLOTLIB)
st.header("Ventas por modelo de iPhone")

colores = [
    "#043556",
    "#FEE9E4",
    "#E4E4EC",
    "#82758E",
    "#F4F8F9",
    "#A19D98"
]

plt.figure()

plt.bar(
    ventas_totales['iPhone_Model'],
    ventas_totales['Quantity'],
    color=colores
)

plt.title(
    'Ventas Totales por Modelo de iPhone '
    '(100 ventas 2025) (MATPLOTLIB)'
)

plt.xlabel('Modelo de iPhone')
plt.ylabel('Cantidad Vendida')

plt.xticks(rotation=45)

st.pyplot(plt)

plt.close()


# GRAFICA DE PASTEL (MATPLOTLIB)
plt.figure()

plt.pie(
    ventas_totales['Quantity'],
    labels=ventas_totales['iPhone_Model'],
    autopct='%1.1f%%',
    colors=colores
)

plt.title(
    'Distribución de Ventas por Modelo de iPhone '
    '(100 ventas 2025) (MATPLOTLIB)'
)

st.pyplot(plt)

plt.close()


# GRAFICA DE BARRAS (SEABORN)
st.header("Visualización con Seaborn")

plt.figure()

sns.set_theme(style="white")

sns.barplot(
    x='iPhone_Model',
    y='Quantity',
    data=ventas_totales,
    palette=colores
)

plt.title(
    'Ventas Totales por Modelo de iPhone '
    '(100 ventas 2025) (Seaborn)'
)

plt.xlabel('Modelo de iPhone')
plt.ylabel('Cantidad Vendida')

plt.xticks(rotation=45)

st.pyplot(plt)

plt.close()


# GRAFICA DE LINEAS (MATPLOTLIB)
st.header("Ventas por mes")

plt.figure()

plt.plot(
    ventas_tiempo['Sale_Date'].astype(str),
    ventas_tiempo['Quantity'],
    marker='o',
    color='#043556'
)

plt.title(
    'Ventas Totales por Mes '
    '(100 ventas 2025) (MATPLOTLIB)'
)

plt.xlabel('Mes')
plt.ylabel('Cantidad Vendida')

plt.xticks(rotation=45)

st.pyplot(plt)

plt.close()


# GRAFICA DE LINEAS (SEABORN)
plt.figure()

sns.set_theme(style="white")

sns.lineplot(
    x=ventas_tiempo['Sale_Date'].astype(str),
    y=ventas_tiempo['Quantity'],
    marker='o', #Sirve para marcar los puntos de datos en la línea
    color='#043556'
)

plt.title(
    'Ventas Totales por Mes '
    '(100 ventas 2025) (Seaborn)'
)

plt.xlabel('Mes')
plt.ylabel('Cantidad Vendida')

plt.xticks(rotation=45)

st.pyplot(plt)

plt.close()

# Correr con "python -m streamlit run limpieza.py"