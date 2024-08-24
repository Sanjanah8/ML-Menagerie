# Residual plot to check the fit of the regression model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict and plot residuals
y_pred = lr.predict(X_test)
residuals = y_test - y_pred

sns.residplot(x=y_pred, y=residuals, lowess=True)
plt.title('Residual Plot')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.show()
