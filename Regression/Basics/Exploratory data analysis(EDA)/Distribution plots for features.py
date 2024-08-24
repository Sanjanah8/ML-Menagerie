# Distribution of numerical features
for column in df.columns:
    if df[column].dtype != 'object':
        sns.histplot(df[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.show()
