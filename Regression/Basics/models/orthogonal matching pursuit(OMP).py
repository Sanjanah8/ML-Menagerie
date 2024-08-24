from sklearn.linear_model import OrthogonalMatchingPursuit

# Initialize the Orthogonal Matching Pursuit model
omp_reg = OrthogonalMatchingPursuit()

# Train the model
omp_reg.fit(X_train, y_train)

# Make predictions
y_pred = omp_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Orthogonal Matching Pursuit Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
