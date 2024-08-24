import seaborn as sns

g = sns.FacetGrid(df, col='categorical_feature', margin_titles=True)
g.map(sns.scatterplot, 'feature_column', 'target_column')
g.set_axis_labels('Feature Column', 'Target Column')
g.set_titles(col_template='{col_name}')
plt.show()
