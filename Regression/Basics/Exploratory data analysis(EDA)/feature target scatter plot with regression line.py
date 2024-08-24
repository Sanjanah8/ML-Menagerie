# Scatter plot with regression line for each feature vs target
for column in df.columns:
    if df[column].dtype != 'object' and column != 'target_column':
        sns.regplot(x=df[column], y=df['target_column'])
        plt.title(f'Scatter Plot with Regression Line of {column} vs Target')
        plt.show()
