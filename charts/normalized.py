import plotly.graph_objects as go

PERIOD_LABELS = {
    "1mo": "1 Month",
    "6mo": "6 Months",
    "1y": "1 Year",
    "2y": "2 Years",
    "5y": "5 Years",
    "10y": "10 Years"
}

def normalized_chart(all_data, default_period="5y"):
    """
    Receives a dictionary {period: {name: Series}} and returns a Plotly figure
    with all periods embedded and buttons to switch between them.
    """
    fig = go.Figure()

    periods = list(all_data.keys())
    assets = list(all_data[periods[0]].keys())
    default_index = periods.index(default_period) if default_period in periods else 0

    for i, period in enumerate(periods):
        data = all_data[period]
        visible = (i == default_index)

        for name, series in data.items():
            normalized = (series / series.iloc[0]) * 100

            fig.add_trace(go.Scatter(
                x=normalized.index,
                y=normalized.values,
                name=name,
                visible=visible,
                legendgroup=name,
                showlegend=True,  # always True — legendgroup handles deduplication
                mode="lines",
                hovertemplate=f"<b>{name}</b><br>Date: %{{x|%b %d, %Y}}<br>Change: %{{customdata:.1f}}%<extra></extra>",
                customdata=normalized.values - 100,
            ))

    # Build visibility masks for each period button
    # Each mask is a list of True/False — one per trace
    n_assets = len(assets)
    buttons = []

    for i, period in enumerate(periods):
        # Only traces belonging to this period should be visible
        visibility = []
        for j in range(len(periods)):
            visibility += [j == i] * n_assets

        buttons.append(dict(
            label=PERIOD_LABELS[period],
            method="update",
            args=[
                {"visible": visibility},
                {"title.text": f"Commodity Dashboard — {PERIOD_LABELS[period]} performance (indexed to 100)"},
            ],
        ))

    fig.update_layout(
        title=dict(
            text=f"Precious metals Dashboard — {PERIOD_LABELS[periods[default_index]]} performance (indexed to 100)",
            y=0.98,
            x=0.5,
            xanchor="center",
            yanchor="top",
        ),
        yaxis_title="Indexed to 100",
        xaxis_title="Date",
        hovermode="x unified",
        margin=dict(t=60, b=60),
        legend=dict(orientation="v", x=1.02, y=1),
        plot_bgcolor="white",
        paper_bgcolor="white",
        yaxis=dict(
            gridcolor="#e8e8e8",
            gridwidth=0.5,
            zerolinecolor="#e8e8e8",
            showline=True,
            linecolor="#cccccc",
            mirror=True,  # draws the line on both sides, creating a full border
        ),
        xaxis=dict(
            gridcolor="#e8e8e8",
            gridwidth=0.5,
            showline=True,
            linecolor="#cccccc",
            mirror=True,
        ),
        colorway=[
            "#2196F3",  # 1st asset
            "#FF5722",  # 2nd asset
            "#4CAF50",  # 3rd asset
            "#9C27B0",  # 4th asset
            "#00BCD4",  # 5th asset
            "#F44336",  # 6th asset
            "#FF9800",  # 7th asset
            "#607D8B",  # 8th asset
        ],
        updatemenus=[dict(
            type="dropdown",
            x=1.02,
            xanchor="left",
            y=0.5,
            yanchor="middle",
            active=periods.index(default_period),
            buttons=buttons,
        )],
    )

    # Reference line at 100 = starting point
    fig.add_hline(y=100, line_dash="dash", line_color="gray", opacity=0.5,
                  annotation_text="Starting point", annotation_position="bottom right")

    return fig