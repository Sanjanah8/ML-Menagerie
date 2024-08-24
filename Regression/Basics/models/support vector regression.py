from sklearn.svm import SVR

# Initialize the Support Vector Regressor
svr = SVR(kernel='rbf', C=1.0, epsilon=0.1)

# Feature scaling is typically required for SVR
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
svr.fit(X_train_scaled, y_train)

# Make predictions
y_pred = svr.predict(X_test_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Support Vector Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
