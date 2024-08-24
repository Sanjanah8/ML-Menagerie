from sklearn.preprocessing import PolynomialFeatures

# Transform the features to polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_train)

# Initialize the Linear Regression model
poly_reg = LinearRegression()

# Train the model on the polynomial features
poly_reg.fit(X_poly, y_train)

# Transform test data and make predictions
X_test_poly = poly.transform(X_test)
y_pred = poly_reg.predict(X_test_poly)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Polynomial Regression - MSE: {mse:.2f}, R2 Score: {r2:.2f}")
