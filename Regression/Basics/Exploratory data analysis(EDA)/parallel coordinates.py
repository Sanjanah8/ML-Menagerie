import pandas as pd
from pandas.plotting import parallel_coordinates

parallel_coordinates(df, 'categorical_feature')
plt.title('Parallel Coordinates Plot')
plt.show()
