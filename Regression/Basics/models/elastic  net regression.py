from sklearn.linear_model import ElasticNet

# Initialize the ElasticNet Regression model
elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)  # l1_ratio controls the mix of Lasso and Ridge

# Train the model
elastic_net.fit(X_train, y_train)

# Make predictions
y_pred = elastic_net.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"ElasticNet Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
