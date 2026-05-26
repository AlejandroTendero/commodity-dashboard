import plotly.graph_objects as go

PERIOD_LABELS = {
    "1mo": "1 Month",
    "6mo": "6 Months",
    "1y": "1 Year",
    "2y": "2 Years",
    "5y": "5 Years",
    "10y": "10 Years"
}

def normalized_chart(data, period_label=""):
    """
    Receives a dictionary {name: Series} for a single period and returns a Plotly figure.
    """
    fig = go.Figure()

    for name, series in data.items():
        normalized = (series / series.iloc[0]) * 100

        fig.add_trace(go.Scatter(
            x=normalized.index,
            y=normalized.values,
            name=name,
            legendgroup=name,
            showlegend=True,  # always True — legendgroup handles deduplication
            mode="lines",
            hovertemplate=f"<b>{name}</b><br>Date: %{{x|%b %d, %Y}}<br>Change: %{{customdata:.1f}}%<extra></extra>",
            customdata=normalized.values - 100,
        ))

    fig.update_layout(
        title=dict(
            text=f"Commodity Dashboard — {period_label} performance (indexed to 100)",
            y=0.98,
            x=0.5,
            xanchor="center",
            yanchor="top",
        ),
        font=dict(color="black"),  # color global del texto
        yaxis_title="Indexed to 100",
        xaxis_title="Date",
        hovermode="x unified",
        margin=dict(t=80, b=80, l=80, r=80),
        legend=dict(
            orientation="v",
            x=0.01,
            y=0.99,
            font=dict(color="black")  # color específico de la leyenda
        ),
        plot_bgcolor="white",
        paper_bgcolor="white",
        yaxis=dict(
            gridcolor="#e8e8e8",
            gridwidth=0.5,
            zerolinecolor="#e8e8e8",
            tickfont=dict(color="black"),
            title_font=dict(color="black"),
            showline=True,
            linecolor="#cccccc",
            mirror=True,  # draws the line on both sides, creating a full border
        ),
        xaxis=dict(
            gridcolor="#e8e8e8",
            gridwidth=0.5,
            showline=True,
            linecolor="#cccccc",
            tickfont=dict(color="black"),
            title_font=dict(color="black"),
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
    )

    # Reference line at 100 = starting point
    fig.add_hline(y=100, line_dash="dash", line_color="gray", opacity=0.5,
                  annotation_text="Starting point", annotation_position="bottom right")

    return fig