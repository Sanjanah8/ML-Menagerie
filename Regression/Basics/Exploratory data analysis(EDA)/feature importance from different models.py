from sklearn.ensemble import ExtraTreesRegressor

# Train Extra Trees Regressor for feature importance
model = ExtraTreesRegressor()
model.fit(X_train, y_train)

# Feature importance plot
importances = model.feature_importances_
indices = np.argsort(importances)

plt.figure(figsize=(12, 8))
plt.title('Feature Importances')
plt.barh(range(X.shape[1]), importances[indices], align='center')
plt.yticks(range(X.shape[1]), [X.columns[i] for i in indices])
plt.xlabel('Feature Importance')
plt.show()
