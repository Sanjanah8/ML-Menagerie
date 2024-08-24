from sklearn.neighbors import KNeighborsRegressor

# Initialize the K-Nearest Neighbors Regressor
knn_reg = KNeighborsRegressor(n_neighbors=5)

# Train the model
knn_reg.fit(X_train, y_train)

# Make predictions
y_pred = knn_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"K-Nearest Neighbors Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
