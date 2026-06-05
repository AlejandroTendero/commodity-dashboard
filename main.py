import streamlit as st
import pandas as pd
from data.fetcher import fetch_data, VALID_PERIODS
from charts.normalized import normalized_chart, PERIOD_LABELS

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

st.subheader("Performance by period")

# Construir la tabla
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
st.dataframe(df_tabla)