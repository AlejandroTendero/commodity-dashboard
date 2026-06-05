import plotly.graph_objects as go
import pandas as pd

def correlation_heatmap(data):
    """
    Receives a dictionary {name: Series} and returns a Plotly correlation heatmap.
    """
    # Construir DataFrame con todos los activos como columnas
    df = pd.DataFrame(data)
    
    # Calcular matriz de correlación
    corr = df.corr()
    
    fig = go.Figure(go.Heatmap(
        z=corr.values,
        x=corr.columns.tolist(),
        y=corr.columns.tolist(),
        colorscale="RdYlGn",
        zmin=-1,
        zmax=1,
        text=corr.values.round(2),
        texttemplate="%{text}",
    ))

    fig.update_layout(
        height=350,
        margin=dict(t=60, b=40, l=40, r=40),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="black"),
    )

    return fig