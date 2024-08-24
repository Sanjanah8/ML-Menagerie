from sklearn.linear_model import RANSACRegressor

# Initialize the RANSAC Regressor
ransac_reg = RANSACRegressor(base_estimator=LinearRegression(), random_state=42)

# Train the model
ransac_reg.fit(X_train, y_train)

# Make predictions
y_pred = ransac_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"RANSAC Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
