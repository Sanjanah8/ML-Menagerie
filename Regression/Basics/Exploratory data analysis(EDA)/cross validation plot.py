from sklearn.model_selection import cross_val_score

# Train a model and perform cross-validation
model = LinearRegression()
cv_scores = cross_val_score(model, X, y, cv=10)

# Plot cross-validation results
plt.plot(cv_scores, 'o-', color='b', label='Cross-Validation Scores')
plt.title('Cross-Validation Scores')
plt.xlabel('Fold')
plt.ylabel('Score')
plt.legend()
plt.show()
