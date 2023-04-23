"""
Input: diabetes-1.csv

PregnancyTImes,Plasma Glucose,Blood Pressure,Triceps thickness,2hr serum insulin,BMI,Pedigree,Age,Class
6,148,72,35,0,33.6,0.627,50,1
1,85,66,29,0,26.6,0.351,31,0

Class is the binary label. 
if 1: the person has diabetes
else: they do not.

Build Classifier for SVM, Decision Trees, ANN

"""
import csv


from sklearn.svm import SVC

"""  Function to read csv file w or w/out header """
def read_csv(file_name):
    data=[]
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        #header = next(reader)
        data = [row for row in reader]
    return data

def split_data():
	pass


"""
Support Vector Machines
Function Input: TrainData, TrainLabels, ValData, ValLabels

Model Input:  * C: regularization parameter (must be positive). The strength of the regularization is inversely proportional to C.
		* kernel: {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'} or callable, default='rbf'

"""
def svm(trainData, trainLabels, valData, valLabels):
	model = SVC(C=0.5, kernel='poly')
	model.fit(trainData, trainLabels)
	score = model.score(valData, valLabels)

	pass

if __name__ == '__main__':
	data = read_csv('./diabetes-1.csv')
	(trainData, testData, trainLabels, testLabels) = split_data(data, )

	i = 0
	for row in data:
		if i < 5:
			i+=1
		else:
			break
		print(row)