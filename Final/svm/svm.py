import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

from sklearn.preprocessing import StandardScaler

# load the dataset
diabetes_df = pd.read_csv('./diabetes-1.csv')

# separate features and target
X = diabetes_df.drop('Class', axis=1)
y = diabetes_df['Class']

# split the data into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=84)
  
#print(f"training data points: {len(y_train)}\nvalidation data points: {len(y_val)}\ntesting data points: {len(y_test)}")
# scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)


# train the model
model = SVC(C=0.5, kernel='poly')
model.fit(X_train, y_train)
score = model.score(X_val, y_val)

# make predictions
predictions = model.predict(X_test)
report = (classification_report(y_test, predictions, output_dict=True))
print(f"Support Vector Machine: \nPrecision: {round(report['weighted avg']['precision'], 2)} \nRecall: {round(report['weighted avg']['recall'],2)}\nF1-score: {round(report['weighted avg']['f1-score'],2)}\n\n")


"""# convert the classification report to a DataFrame
report_df = pd.DataFrame(report).transpose()
# remove the 'support' column
report_df = report_df.drop('support', axis=1)

# plot the heatmap using seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(report_df, annot=True, cmap='coolwarm', cbar=False, fmt='.2f')
plt.title('Support Vector Machine Classification Report Heatmap')
plt.xlabel('Metrics')
plt.ylabel('Classes')
plt.show()"""
