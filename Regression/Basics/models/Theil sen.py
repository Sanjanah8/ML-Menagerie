from sklearn.linear_model import TheilSenRegressor

# Initialize the Theil-Sen Regressor
theil_sen_reg = TheilSenRegressor(random_state=42)

# Train the model
theil_sen_reg.fit(X_train, y_train)

# Make predictions
y_pred = theil_sen_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Theil-Sen Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
