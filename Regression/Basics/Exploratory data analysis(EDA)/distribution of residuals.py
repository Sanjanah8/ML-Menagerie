# Plot the distribution of residuals to check for normality
sns.histplot(residuals, kde=True)
plt.title('Distribution of Residuals')
plt.show()
