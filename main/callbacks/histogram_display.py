from dash import callback, Output, Input
import plotly.express as px
import pandas as pd

# Time thresholds (matching buttons_nextFlashcard.py)
TIME_GREEN = 1.5
TIME_YELLOW = 2.7
TIME_PURPLE = 5.0

def get_bar_colors(times):
    colors = []
    for t in times:
        if t < TIME_GREEN:
            colors.append("#90EE90")      # Light green
        elif t < TIME_YELLOW:
            colors.append("#FFEB3B")      # Pure yellow
        elif t < TIME_PURPLE:
            colors.append("#FF6200")      # Pure intense orange
        else:
            colors.append("#DDA0DD")      # Plum
    return colors

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
        y='session_time',
        range_y=[0, 5],    # Changed from 10 to 5
        height=100         # Increased from 80 to 100
    )
    
    # Update bar colors
    fig.update_traces(marker_color=get_bar_colors(df['session_time']))
    
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