# Heatmap to check for multicollinearity
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Multicollinearity Heatmap')
plt.show()
