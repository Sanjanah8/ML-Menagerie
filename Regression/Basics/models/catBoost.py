from catboost import CatBoostRegressor

# Initialize the CatBoost Regressor
catboost_reg = CatBoostRegressor(iterations=100, learning_rate=0.1, random_seed=42, verbose=0)

# Train the model
catboost_reg.fit(X_train, y_train)

# Make predictions
y_pred = catboost_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"CatBoost Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
