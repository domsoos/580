import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV


# ge the file, check if it exist
current_directory = os.getcwd()
csv_file_path = os.path.join(current_directory, 'diabetes-1.csv')
if not os.path.exists(csv_file_path):
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)
    print("Moved to parent directory:", os.getcwd())

# load the dataset
diabetes_df = pd.read_csv('./diabetes-1.csv')

# separate features and target
X = diabetes_df.drop('Class', axis=1)
y = diabetes_df['Class']

# split the data into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=84)

print(f"training data points: {len(y_train)}\nvalidation data points: {len(y_val)}\ntesting data points: {len(y_test)}")


# scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)


# get the best model
param_grid = {'C': [0.5, 0.1, 1, 10, 100], 'kernel': ['linear', 'poly', 'rbf', 'sigmoid'], 'gamma': ['scale', 'auto']}
grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)
grid.fit(X_train, y_train)

# Use the best model found by GridSearchCV
best_model = grid.best_estimator_
score = best_model.score(X_val, y_val)


# Make predictions
predictions = best_model.predict(X_test)
print("Evaluation on Testing Data")
report = (classification_report(y_test, predictions, output_dict=True))
print(report)

# Convert the classification report to a DataFrame
report_df = pd.DataFrame(report).transpose()

# Remove the 'support' column
report_df = report_df.drop('support', axis=1)

# Plot the heatmap using seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(report_df, annot=True, cmap='coolwarm', cbar=False, fmt='.2f')
plt.title('Classification Report Heatmap')
plt.xlabel('Metrics')
plt.ylabel('Classes')
plt.show()


