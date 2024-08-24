from lightgbm import LGBMRegressor

# Initialize the LightGBM Regressor
lgbm_reg = LGBMRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

# Train the model
lgbm_reg.fit(X_train, y_train)

# Make predictions
y_pred = lgbm_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"LightGBM Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
