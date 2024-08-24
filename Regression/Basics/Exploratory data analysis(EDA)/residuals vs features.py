# Scatter plot of residuals vs each feature
for column in df.columns:
    if df[column].dtype != 'object' and column != 'target_column':
        sns.scatterplot(x=df[column], y=residuals)
        plt.title(f'Residuals vs {column}')
        plt.show()
