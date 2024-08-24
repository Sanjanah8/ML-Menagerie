# Check for missing values
print(df.isnull().sum())

# Option 1: Drop missing values
df = df.dropna()

# Option 2: Fill missing values
df = df.fillna(df.median())

#encoding categorical variables

# Label encoding for binary categorical variables
label_encoder = LabelEncoder()
df['Binary_Category'] = label_encoder.fit_transform(df['Binary_Category'])

# One-hot encoding for multi-class categorical variables
df = pd.get_dummies(df, columns=['Multi_Class_Category'], drop_first=True)

#Feature selection 

# Define feature columns and target variable
features = ['Feature1', 'Feature2', 'Feature3']
target = 'Target_Variable'

X = df[features]
y = df[target]
