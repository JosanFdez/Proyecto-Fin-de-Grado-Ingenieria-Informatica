import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos clasificados
df = pd.read_csv("modelos_clasificados_clusters.csv")

st.set_page_config(page_title="Análisis de Aeronaves", layout="wide")
st.title("Análisis de tipos de aeronaves comerciales")

# Filtros
cluster_sel = st.multiselect("Seleccionar clusters", sorted(df['cluster'].unique()), default=df['cluster'].unique())
df_filtrado = df[df['cluster'].isin(cluster_sel)]

# Métricas clave
col1, col2, col3 = st.columns(3)
col1.metric("Modelos únicos", len(df_filtrado))
col2.metric("Vuelos totales", int(df_filtrado['vuelos'].sum()))
col3.metric("Duración promedio global", f"{df_filtrado['duracion_media'].mean():.1f} min")

# Mapa PCA
fig_pca = px.scatter(df_filtrado, x="pca1", y="pca2", color="cluster", size="vuelos", hover_data=["tipo"])
st.plotly_chart(fig_pca, use_container_width=True)

# Comparación de duración media
fig_dur = px.box(df_filtrado, x="cluster", y="duracion_media", color="cluster", points="all")
st.plotly_chart(fig_dur, use_container_width=True)

# Tabla
st.subheader("Detalle por tipo de aeronave")
st.dataframe(df_filtrado.sort_values(by="vuelos", ascending=False), use_container_width=True)
