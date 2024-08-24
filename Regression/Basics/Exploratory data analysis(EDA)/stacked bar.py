import matplotlib.pyplot as plt

df.groupby('categorical_feature')['target_column'].sum().unstack().plot(kind='bar', stacked=True)
plt.title('Stacked Bar Plot')
plt.xlabel('Categorical Feature')
plt.ylabel('Sum of Target Column')
plt.show()
