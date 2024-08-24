# Feature interaction plot (bivariate feature vs target)
sns.lmplot(x='feature1', y='feature2', hue='target_column', data=df)
plt.title('Feature Interaction Plot')
plt.show()
