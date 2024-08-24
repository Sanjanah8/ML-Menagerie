from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import plot_partial_dependence

# Train a gradient boosting model
gbm = GradientBoostingRegressor()
gbm.fit(X_train, y_train)

# Partial dependence plot
features = [0, 1]  # Indices of the features you want to plot
fig, ax = plt.subplots(figsize=(12, 8))
plot_partial_dependence(gbm, X_train, features, ax=ax)
plt.show()
