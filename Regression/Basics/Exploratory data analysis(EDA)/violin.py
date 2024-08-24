# Violin plot to visualize the distribution of the target across categorical features
for column in df.columns:
    if df[column].dtype == 'object':
        sns.violinplot(x=df[column], y=df['target_column'])
        plt.title(f'Violin Plot of {column} vs Target')
        plt.show()
