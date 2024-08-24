from lightgbm import LGBMRegressor

# Initialize the LightGBM Regressor with early stopping
lgbm_reg = LGBMRegressor(n_estimators=1000, learning_rate=0.01, random_state=42)

# Fit model with early stopping
lgbm_reg.fit(X_train, y_train, 
             eval_set=[(X_test, y_test)],
             eval_metric='l2',
             early_stopping_rounds=50,
             verbose=0)

# Make predictions
y_pred = lgbm_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"LGBM with Early Stopping - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
