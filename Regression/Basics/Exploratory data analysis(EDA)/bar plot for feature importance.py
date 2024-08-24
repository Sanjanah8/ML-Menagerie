# Feature importance using RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

# Assuming 'target_column' is your target variable
X = df.drop('target_column', axis=1)
y = df['target_column']

# Encoding categorical variables (if any)
X = pd.get_dummies(X)

# Train a random forest model
model = RandomForestRegressor()
model.fit(X, y)

# Plot feature importances
importance = model.feature_importances_
indices = np.argsort(importance)

plt.figure(figsize=(10, 6))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importance[indices], align='center')
plt.yticks(range(len(indices)), [X.columns[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()
