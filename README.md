# Commodity Dashboard

An interactive dashboard to compare the performance of commodities and the S&P 500 over time — no installation required.

**[View live dashboard](https://commodity-webapp-tendero.streamlit.app/)**

---

## What it shows

All assets are normalized to a base of 100 at the start of the selected period. This makes it easy to compare percentage growth across assets with very different price levels — the chart answers the question: *if you had invested $100 in each asset at the start of this period, where would you be today?*

| Asset | Ticker | Type |
|-------|--------|------|
| Gold | GC=F | Continuous futures |
| Silver | SI=F | Continuous futures |
| Platinum | PL=F | Continuous futures |
| Palladium | PA=F | Continuous futures |
| Copper | HG=F | Continuous futures |
| Oil (WTI) | CL=F | Continuous futures |
| Natural Gas | NG=F | Continuous futures |
| S&P 500 | ^GSPC | Index |

**Available periods:** 1 Month · 6 Months · Year to Date · 1 Year · 2 Years · 5 Years · 10 Years

---

## Features

- **Normalized performance chart** — compare assets from a common starting point
- **Asset selector** — choose which commodities to display; S&P 500 always shown as reference
- **Performance table** — returns for every available period, color-coded green/red, with the active period highlighted
- **Correlation matrix** — heatmap showing how selected assets move in relation to each other

---

## How it works

The app is built with Streamlit and fetches data in real time from Yahoo Finance on each session. No pre-generated files — data is always current.