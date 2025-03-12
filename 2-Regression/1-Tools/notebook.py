from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.datasets import load_linnerud
from sklearn.model_selection import train_test_split

# Load the dataset
X, y = load_linnerud(return_X_y=True, as_frame=False)

# Select a single feature (e.g., the third feature)
X = X[:, [2]]
# If desired, also select a single target (e.g., the first target)
y = y[:, [1]]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle=False)

# Fit the regression model
regressor = LinearRegression().fit(X_train, y_train)

# Predict on the test set
y_pred = regressor.predict(X_test)

# Plot the results
plt.scatter(X_test, y_test, color='black', label='Actual Data')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regression Line')
plt.xlabel('Selected Feature')
plt.ylabel('Selected Target')
plt.title('Regression of Selected Target on Selected Feature')
plt.legend()
plt.show()
