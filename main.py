from data.fetcher import fetch_all_periods
from charts.normalized import normalized_chart

# --- Configuration ---
OUTPUT_PATH = "docs/normalized.html"

# --- Run ---
data = fetch_all_periods()
fig = normalized_chart(data)
fig.write_html(OUTPUT_PATH)

print(f"Chart saved to {OUTPUT_PATH}")