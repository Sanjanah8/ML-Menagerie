from sklearn.metrics import roc_curve, auc

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Predict and compute residuals
y_pred = model.predict(X_test)
residuals = y_test - y_pred

# Compute cumulative gain
# (Note: Cumulative gain plot is more commonly used for classification; however, a similar approach can be used for regression.)

plt.plot(np.sort(y_pred), np.cumsum(np.sort(y_test)))
plt.title('Cumulative Gain Plot')
plt.xlabel('Predicted')
plt.ylabel('Cumulative Gain')
plt.show()
