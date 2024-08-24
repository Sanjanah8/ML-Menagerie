# Countplot for categorical features
for column in df.columns:
    if df[column].dtype == 'object':
        sns.countplot(x=df[column])
        plt.title(f'Countplot of {column}')
        plt.show()
