from data.fetcher import fetch_data
from charts.normalized import normalized_chart

# --- Configuration ---
PERIOD = "5y"
OUTPUT_PATH = "docs/normalized.html"

# --- Run ---
data = fetch_data(period=PERIOD)
fig = normalized_chart(data, period=PERIOD)
fig.write_html(OUTPUT_PATH)

print(f"Chart saved to {OUTPUT_PATH}")