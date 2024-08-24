# Boxplots to detect outliers in numerical features
for column in df.columns:
    if df[column].dtype != 'object':
        sns.boxplot(x=df[column])
        plt.title(f'Boxplot of {column}')
        plt.show()
