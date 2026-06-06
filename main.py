import streamlit as st
import pandas as pd
from data.fetcher import fetch_data, VALID_PERIODS
from charts.normalized import normalized_chart, PERIOD_LABELS
from charts.heatmap import correlation_heatmap

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .block-container { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.title("Commodity dashboard")

data = fetch_data("5y")  # para poblar el multiselect

with st.sidebar:
    st.header("Controls")
    periodo = st.selectbox(
        "Select period",
        options=VALID_PERIODS,
        format_func=lambda p: PERIOD_LABELS[p],
        index=VALID_PERIODS.index("1y")
    )
    activos_seleccionados = st.multiselect(
        "Select assets",
        options=[a for a in data.keys() if a != "S&P 500"],
        default=["Gold", "Silver"]
    )

data = fetch_data(periodo)  # recalcula con el periodo real

# S&P 500 siempre incluido
data_filtrada = {k: v for k, v in data.items() if k == "S&P 500" or k in activos_seleccionados}
fig = normalized_chart(data_filtrada, period_label=PERIOD_LABELS[periodo])

st.plotly_chart(fig, width='stretch', height=550)

def color_rendimiento(val):
    try:
        num = float(val.replace("%", "").replace("+", ""))
        color = "green" if num > 0 else "red" if num < 0 else "black"
        return f"color: {color}"
    except:
        return ""

st.subheader("Performance by period")
rows = []
for p in VALID_PERIODS:
    data_p = fetch_data(p)
    row = {"Period": PERIOD_LABELS[p]}
    activos_tabla = activos_seleccionados + ["S&P 500"]
    for activo in activos_tabla:
        if activo in data_p:
            series = data_p[activo]
            rendimiento = (series.iloc[-1] / series.iloc[0] - 1) * 100
            row[activo] = f"{rendimiento:+.1f}%"
    rows.append(row)
df_tabla = pd.DataFrame(rows).set_index("Period")
ancho_columna = 120
ancho_total = ancho_columna * (len(activos_seleccionados) + 1)
def resaltar_fila(row):
    if row.name == PERIOD_LABELS[periodo]:
        return ["background-color: #f0f0f0; font-weight: bold"] * len(row)
    return [""] * len(row)
st.dataframe(
    df_tabla.style.map(color_rendimiento).apply(resaltar_fila, axis=1),
    width=ancho_total
)

st.subheader("Correlation matrix")
fig_heatmap = correlation_heatmap(data_filtrada)
st.plotly_chart(fig_heatmap, width="content")