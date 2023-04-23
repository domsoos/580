import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

from sklearn.preprocessing import StandardScaler

current_directory = os.getcwd()

# Check if the CSV file exists in the current working directory
csv_file_path = os.path.join(current_directory, 'diabetes-1.csv')
if not os.path.exists(csv_file_path):
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)

diabetes_df = pd.read_csv('./diabetes-1.csv')

# Separate the features and target
X = diabetes_df.drop('Class', axis=1)
y = diabetes_df['Class']


# Scale the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=84)

#print(f"training data points: {len(y_train)}\nvalidation data points: {len(y_val)}\ntesting data points: {len(y_test)}")

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)


# Train the model using DecisionTreeClassifier
model = DecisionTreeClassifier(min_samples_leaf=8, random_state=42)
model.fit(X_train, y_train)
score = model.score(X_val, y_val)

# Make predictions
predictions = model.predict(X_test)
#print("Evaluation on Testing Data")
report = (classification_report(y_test, predictions, output_dict=True))
#print(report)

print(f"\n\nDecision Trees: \nPrecision: {round(report['weighted avg']['precision'], 2)} \nRecall: {round(report['weighted avg']['recall'],2)}\nF1-score: {round(report['weighted avg']['f1-score'],2)}\n\n")


# Convert the classification report to a DataFrame
report_df = pd.DataFrame(report).transpose()

# Remove the 'support' column
report_df = report_df.drop('support', axis=1)

# Plot the heatmap using seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(report_df, annot=True, cmap='coolwarm', cbar=False, fmt='.2f')
plt.title('Decision Trees Classification Report Heatmap')
plt.xlabel('Metrics')
plt.ylabel('Classes')
plt.show()
