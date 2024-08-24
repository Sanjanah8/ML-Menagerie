# Boxplots to visualize distribution of target variable across different categories
for column in df.columns:
    if df[column].dtype == 'object':
        sns.boxplot(x=df[column], y=df['target_column'])
        plt.title(f'Boxplot of {column} vs Target')
        plt.show()
