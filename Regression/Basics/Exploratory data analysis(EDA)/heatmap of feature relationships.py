# Heatmap of pairwise feature relationships using seaborn
sns.heatmap(df.drop(columns='target_column').corr(), annot=True, cmap='coolwarm')
plt.title('Feature Relationship Heatmap')
plt.show()
