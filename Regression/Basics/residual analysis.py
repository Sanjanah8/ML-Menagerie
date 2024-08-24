# Plot residuals
residuals = y_test - y_pred_lr

plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True)
plt.title("Residuals Distribution")
plt.show()

# Residuals vs Fitted Values
plt.figure(figsize=(10, 6))
plt.scatter(y_pred_lr, residuals, alpha=0.6, color='purple')
plt.axhline(0, linestyle='--', color='red')
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted Values")
plt.show()
