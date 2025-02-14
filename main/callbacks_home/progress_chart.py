from dash import Input, Output, callback
import pandas as pd
import plotly.express as px
import numpy as np

@callback(
    Output('progress-chart', 'figure'),
    Input('progress-chart', 'id')
)
def update_progress_chart(_):
    """Create sedimentation chart showing how word durations change over time"""
    # Load the distribution data
    df = pd.read_csv('main/duration_distribution.csv')
    df['date'] = pd.to_datetime(df['date'])
    
    # Group the 0.1s buckets into meaningful categories
    duration_ranges = {
        'Very Fast (0-1.5s)': [f'duration_{i:.1f}' for i in np.arange(0  , 1.5 , 0.1)],
        'Fast (1.5-2.7s)':    [f'duration_{i:.1f}' for i in np.arange(1.5, 2.7 , 0.1)],
        'Medium (2.7-5.0s)':  [f'duration_{i:.1f}' for i in np.arange(2.7, 5.0 , 0.1)],
        'Slow (5.0-10.0s)':   [f'duration_{i:.1f}' for i in np.arange(5.0, 9.8, 0.1)]
    }
    
    # Sum up the columns in each category
    for category, columns in duration_ranges.items():
        df[category] = df[columns].sum(axis=1)
    
    # Create the stacked bar chart
    fig = px.bar(
        df,
        x='date',
        y=list(duration_ranges.keys()),
        title='Word Response Time Distribution',
        labels={'date': 'Date', 'value': 'Number of Words'},
        color_discrete_sequence=['#90EE90', '#FFEB3B', '#FF6200', '#DDA0DD']
    )
    
    # Update layout
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        title_x=0.5,  # Center the title
        legend_title_text='Response Times',
        xaxis_title='Date',
        yaxis_title='Number of Words',
        hovermode='x unified'
    )
    
    return fig 