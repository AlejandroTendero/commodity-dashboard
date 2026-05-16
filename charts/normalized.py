import plotly.graph_objects as go

def normalized_chart(data_by_period: dict, default_period: str = "5y"):
    """
    Receives a dict of dicts: {period: {name: pandas Series}}
    Builds a single Plotly figure with all periods embedded.
    Buttons control which period's traces are visible.
    """
    fig = go.Figure()
    
    periods = list(data_by_period.keys())
    assets = list(data_by_period[default_period].keys())
    
    # --- 1. Add ALL traces for ALL periods ---
    # Why: Plotly needs all data in the HTML from the start.
    # Interactivity is just showing/hiding — no data is fetched later.
    for period in periods:
        is_default = (period == default_period)
        for name, series in data_by_period[period].items():
            normalized = (series / series.iloc[0]) * 100
            fig.add_trace(go.Scatter(
                x=normalized.index,
                y=normalized.values,
                name=name,
                mode="lines",
                visible=is_default,  # Only the default period is visible at start
                legendgroup=name,    # Groups same asset across periods — cleaner legend
                showlegend=is_default,
                hovertemplate=f"<b>{name}</b><br>Date: %{{x|%b %d, %Y}}<br>Change: %{{customdata:.1f}}%<extra></extra>",
                customdata=normalized.values - 100
            ))
    
    # --- 2. Build the visibility array for each button ---
    # Why: Plotly buttons work by passing a list of True/False — one per trace,
    # in the same order they were added. We need to reconstruct that order.
    n_assets = len(assets)
    buttons = []
    
    for i, period in enumerate(periods):
        # For this period: True for its traces, False for everyone else's
        visible = [False] * (n_assets * len(periods))
        for j in range(n_assets):
            visible[i * n_assets + j] = True
        
        buttons.append(dict(
            label=period,
            method="update",  # "update" can change both data properties and layout
            args=[
                {"visible": visible},
                {"title": f"Commodity Dashboard — {period} performance (indexed to 100)"}
            ]
        ))
    
    # --- 3. Add buttons to the layout ---
    fig.update_layout(
        title=f"Commodity Dashboard — {default_period} performance (indexed to 100)",
        yaxis_title="Indexed to 100",
        xaxis_title="Date",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        updatemenus=[dict(
            type="buttons",
            direction="right",
            x=0.0,
            y=1.15,
            showactive=True,  # Highlights the active button
            buttons=buttons
        )]
    )
    
    fig.add_hline(y=100, line_dash="dash", line_color="gray", opacity=0.5,
                  annotation_text="Starting point", annotation_position="bottom right")
    
    return fig