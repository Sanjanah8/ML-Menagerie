# 3D scatter plot for three features and target variable
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['feature1'], df['feature2'], df['target_column'])
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Target')
plt.title('3D Scatter Plot of Feature1 and Feature2 vs Target')
plt.show()
