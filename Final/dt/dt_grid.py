import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report


from sklearn.model_selection import GridSearchCV


# Load the diabetes dataset
diabetes_df = pd.read_csv('./diabetes-1.csv')

# Separate the features and target
X = diabetes_df.drop('Class', axis=1)
y = diabetes_df['Class']

# Split the data into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=84)

print(f"training data points: {len(y_train)}\nvalidation data points: {len(y_val)}\ntesting data points: {len(y_test)}")

# Train the model using DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)
score = model.score(X_val, y_val)

param_grid = {'max_depth': list(range(1, 10)), 'min_samples_split': list(range(2, 10)), 'min_samples_leaf': list(range(1, 10))}
grid = GridSearchCV(DecisionTreeClassifier(), param_grid, refit=True, verbose=2)
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
