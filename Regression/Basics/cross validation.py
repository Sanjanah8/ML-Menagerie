# Perform cross-validation for the Linear Regression model
cv_scores = cross_val_score(lr_model, X, y, cv=5, scoring='r2')
print(f"Cross-Validation R-squared Scores: {cv_scores}")
print(f"Average R-squared Score: {cv_scores.mean():.2f}")
