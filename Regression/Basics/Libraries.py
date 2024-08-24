pip install pandas numpy matplotlib seaborn scikit-learn

# Core Libraries
import pandas as pd   # Data manipulation and analysis
import numpy as np    # Numerical computations

# Visualization Libraries
import matplotlib.pyplot as plt   # Basic plotting
import seaborn as sns             # Statistical data visualization

# Scikit-Learn Libraries
from sklearn.model_selection import train_test_split   # Split dataset into training and testing sets
from sklearn.model_selection import cross_val_score    # Cross-validation
from sklearn.model_selection import GridSearchCV       # Hyperparameter tuning

from sklearn.preprocessing import StandardScaler       # Feature scaling
from sklearn.preprocessing import LabelEncoder         # Encoding binary categorical variables
from sklearn.preprocessing import OneHotEncoder        # Encoding multi-class categorical variables

from sklearn.linear_model import LinearRegression      # Linear regression model
from sklearn.linear_model import Ridge                 # Ridge regression model
from sklearn.linear_model import Lasso                 # Lasso regression model

from sklearn.metrics import mean_squared_error         # Calculate mean squared error (MSE)
from sklearn.metrics import r2_score                   # Calculate R-squared score

from sklearn.pipeline import Pipeline                  # Create pipelines
from sklearn.compose import ColumnTransformer          # Apply different preprocessing steps to different feature columns
