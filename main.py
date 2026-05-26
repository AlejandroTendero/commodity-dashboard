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

fig = normalized_chart(data, period_label=PERIOD_LABELS[periodo])

st.plotly_chart(fig, width='stretch', height=550)
