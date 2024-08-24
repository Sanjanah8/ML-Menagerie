import plotly.express as px

# Interactive scatter plot with Plotly
fig = px.scatter(df, x='feature_column', y='target_column', trendline='ols', title='Interactive Scatter Plot')
fig.show()
