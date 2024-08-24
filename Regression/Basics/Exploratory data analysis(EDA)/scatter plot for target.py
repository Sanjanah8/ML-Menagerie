# Scatter plots for numerical features vs target
for column in df.columns:
    if df[column].dtype != 'object':
        sns.scatterplot(x=df[column], y=df['target_column'])
        plt.title(f'{column} vs Target')
        plt.show()
