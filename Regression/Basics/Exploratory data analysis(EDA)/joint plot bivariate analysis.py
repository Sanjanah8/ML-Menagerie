# Joint plot between feature and target
for column in df.columns:
    if df[column].dtype != 'object':
        sns.jointplot(x=df[column], y=df['target_column'], kind='reg', height=6)
        plt.title(f'Joint Plot of {column} vs Target')
        plt.show()
