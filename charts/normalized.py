import plotly.graph_objects as go

def normalized_chart(data, start_date="2021-01-01"):
    """
    Receives a dictionary {name: pandas Series} and returns
    a Plotly figure with all assets normalized to 100 at start_date.
    """
    fig = go.Figure()

    for name, series in data.items():
        # Normalize to 100 at the first data point → shows % change over time
        normalized = (series / series.iloc[0]) * 100

        fig.add_trace(go.Scatter(
            x=normalized.index,
            y=normalized.values,
            name=name,
            mode="lines",
            hovertemplate=f"<b>{name}</b><br>Date: %{{x|%b %d, %Y}}<br>Change: %{{customdata:.1f}}%<extra></extra>",
            customdata=normalized.values - 100  # actual % change from starting point
        ))

    fig.update_layout(
        title=f"Gold vs Silver vs S&P 500 — % change since {start_date}",
        yaxis_title="Indexed to 100",
        xaxis_title="Date",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    # Reference line at 100 = starting point
    fig.add_hline(y=100, line_dash="dash", line_color="gray", opacity=0.5,
                  annotation_text="Starting point", annotation_position="bottom right")

    return fig