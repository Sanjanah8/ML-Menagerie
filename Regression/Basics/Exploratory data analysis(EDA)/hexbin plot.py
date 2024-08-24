import matplotlib.pyplot as plt

plt.hexbin(df['feature_column'], df['target_column'], gridsize=50, cmap='Blues')
plt.colorbar(label='Count')
plt.xlabel('Feature Column')
plt.ylabel('Target Column')
plt.title('Hexbin Plot')
plt.show()
