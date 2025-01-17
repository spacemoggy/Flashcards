from dash import callback, Output, Input
import plotly.express as px
import pandas as pd

@callback(
    Output('time-histogram', 'figure'),
    Input('word-data', 'data')
)
def update_histogram(word_data):
    df = pd.DataFrame(word_data)
    
    # If session_time doesn't exist yet, create it with zeros
    if 'session_time' not in df.columns:
        df['session_time'] = 0
    
    # Create bar chart
    fig = px.bar(
        df,
        y='session_time',  # Using session_time for bar heights
        range_y=[0, 10],   # Fixed range for consistency
        height=80          # Match layout height
    )
    
    # Update layout
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),  # Minimal margins
        showlegend=False,
        xaxis_title="",
        yaxis_title="",
        xaxis_showticklabels=False,  # Hide x-axis labels
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot
        bargap=0.1  # Gap between bars
    )
    
    return fig 