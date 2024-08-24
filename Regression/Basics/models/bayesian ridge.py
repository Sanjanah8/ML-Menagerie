from sklearn.linear_model import BayesianRidge

# Initialize the Bayesian Ridge Regression model
bayesian_ridge = BayesianRidge()

# Train the model
bayesian_ridge.fit(X_train, y_train)

# Make predictions
y_pred = bayesian_ridge.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Bayesian Ridge Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
