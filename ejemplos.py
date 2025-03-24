import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def base():
    # Crear datos simples
    data = {'categoría': ['A', 'B', 'C', 'D'], 'valor': [10, 15, 13, 8]}

    # Crear gráfico de barras
    fig = px.bar(data, x='categoría', y='valor', title="Gráfico de barras")

    # Mostrar gráfico
    st.plotly_chart(fig)

def grafico_lineas():
    # Datos de ejemplo
    df = px.data.gapminder()
    fig = px.bar(df, x='continent', y='pop', color='continent', title="Población del continente")
    fig.update_layout(
        title="Población total por continente",
        xaxis_title="Continente",
        yaxis_title="Poblacion",
        template="plotly_dark" # Cambio de tema
    )
    # Mostrar el gráfico
    st.plotly_chart(fig)

def scatter():
    # Datos de ejemplo
    df = px.data.iris()
    # Selector de especie
    species = st.selectbox('Selecciona una especie', df['species'].unique())
    # Filtrar los datos
    filtered_df = df[df['species'] == species]
    # Crear gráfico de dispersión filtrado
    fig = px.scatter(filtered_df, x='sepal_width', y='sepal_length', color='species', title=f"Gráfico de dispersión de {species}")
    # Mostrar gráfico
    st.plotly_chart(fig)

def poblaciones():

    # Datos de ejemplo
    df = px.data.gapminder()

    # Crear un gráfico de mapa de burbujas usando graph_objects
    fig = go.Figure(go.Scattergeo(
        locations=df['iso_alpha'],
        size=df['pop'] / 1000000,
        text=df['country'],
        hoverinfo='text',
        marker=dict(color=df['continent'].map({'Asia': 'red', 'Europe': 'blue', 'Africa': 'green', 'Americas': 'yellow'}))
    ))

    # Configurar el gráfico
    fig.update_layout(
        geo=dict(showland=True, landcolor='rgb(255, 255, 255)'),
        title="Mapa de burbujas de la población mundial"
    )

    # Mostrar el gráfico en Streamlit
    click_data = st.plotly_chart(fig, use_container_width=True)

    # Mostrar los datos del clic
    if click_data:
        if "points" in click_data:
            selected_point = click_data["points"][0]
            selected_country = selected_point['hovertext']
            selected_pop = selected_point['marker.size']

            # Mostrar los datos del punto clicado
            st.write(f"Has seleccionado: {selected_country}")
            st.write(f"Población: {selected_pop}")
