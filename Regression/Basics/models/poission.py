from sklearn.linear_model import PoissonRegressor

# Initialize the Poisson Regressor
poisson_reg = PoissonRegressor()

# Train the model
poisson_reg.fit(X_train, y_train)

# Make predictions
y_pred = poisson_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Poisson Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
