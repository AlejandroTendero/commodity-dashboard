import streamlit as st
from data.fetcher import fetch_data, VALID_PERIODS
from charts.normalized import normalized_chart, PERIOD_LABELS

st.title("Commodity dashboard")
periodo = st.selectbox(
            "Select period",
             options=VALID_PERIODS,
             format_func=lambda p: PERIOD_LABELS[p]
        )

data = fetch_data(periodo)

activos_seleccionados = st.multiselect(
    "Select assets",
    options=[a for a in data.keys() if a != "S&P 500"],
    default=["Gold", "Silver"]
)

# S&P 500 siempre incluido
data_filtrada = {k: v for k, v in data.items() if k == "S&P 500" or k in activos_seleccionados}
fig = normalized_chart(data_filtrada, period_label=PERIOD_LABELS[periodo])

st.plotly_chart(fig, width='stretch', height=550)
