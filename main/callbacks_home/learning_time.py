from dash import Input, Output, callback
import pandas as pd
import plotly.express as px

@callback(
    Output('learning-time-chart', 'figure'),
    Input('learning-time-chart', 'id')
)
def update_learning_time_chart(_):
    """Create stacked bar chart showing daily learning time by duration category"""
    # Load learning history
    df = pd.read_csv('main/learning_history.csv')
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    
    # Categorize durations
    categories = [
        'Very Fast (0-1.5s)',
        'Fast (1.5-2.7s)',
        'Medium (2.7-5.0s)',
        'Slow (5.0-10.0s)'
    ]
    
    def get_duration_category(duration):
        if duration < 1.5:
            return categories[0]  # Very Fast
        elif duration < 2.7:
            return categories[1]  # Fast
        elif duration < 5.0:
            return categories[2]  # Medium
        return categories[3]      # Slow
    
    df['category'] = df['actual_duration'].apply(get_duration_category)
    
    # Group by date and category, sum seconds then convert to minutes
    daily_times = df.groupby(['date', 'category'])['actual_duration'].sum().reset_index()
    daily_times['actual_duration'] = daily_times['actual_duration'] / 60
    
    # Create stacked bar chart
    fig = px.bar(
        daily_times,
        x='date',
        y='actual_duration',
        color='category',
        category_orders={'category': categories},  # Force category order
        title='Daily Learning Time by Response Speed',
        labels={'date': 'Date', 'actual_duration': 'Total Time (minutes)'},
        color_discrete_sequence=['#90EE90', '#FFEB3B', '#FF6200', '#DDA0DD']
    )
    
    return fig 