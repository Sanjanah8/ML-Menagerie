from sklearn.linear_model import HuberRegressor

# Initialize the Huber Regressor
huber_reg = HuberRegressor()

# Train the model
huber_reg.fit(X_train, y_train)

# Make predictions
y_pred = huber_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Huber Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
