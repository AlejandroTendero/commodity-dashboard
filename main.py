from data.fetcher import fetch_all_periods
from charts.normalized import normalized_chart

data_by_period = fetch_all_periods()

fig = normalized_chart(data_by_period, default_period="5y")
fig.write_html("docs/normalized.html")