from data.fetcher import fetch_data
from charts.normalized import normalized_chart

# --- Configuration ---
START_DATE = "2021-01-01"
OUTPUT_PATH = "docs/normalized.html"

# --- Run ---
data = fetch_data(start_date=START_DATE)
fig = normalized_chart(data, start_date=START_DATE)
fig.write_html(OUTPUT_PATH)

print(f"Chart saved to {OUTPUT_PATH}")