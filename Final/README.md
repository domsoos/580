
### The code and preprocessing
The shell script can execute all three classifiers, just have to give it permission to execute.

```bash
chmod +x run.sh
```

then, execute the shell script in Linux environment:   
```bash
./run.sh
```   
The figures can be replicated by commenting out the lines starting with plt. 

Initially, the training set was 75% of the entire data and the validation from the training set was 10%, then it increased by 5% which showed significant improvement in some classification models including Decision Tree and Neural Network, but it made SVM’s performance worse. 
Each classifier performed better after scaling the input.


### Support Vector Machines
The Support Vector Machine is known for its effectiveness in high-dimensional spaces. 
After experimenting with the different settings following the original documentation of the sklearn package. The best performance was achieved with a linear kernel and a regularization parameter C = 100, resulting in a precision of 75%, recall of 75%, and an F1-score of 74%. These results indicate that the SVM classifier is effective in distinguishing between individuals with and without diabetes.

| SVM | Linear | | | Poly | | | RBF | | | Sigmoid | | |
| --- | ------ | - | - | ---- | - | - | --- | - | - | ------- | - | - |
| C   | P      | R | F1 | P    | R | F1 | P   | R | F1 | P     | R | F1 |
| 0.5 | .73    | .73| .73| .75  | .75| .73| .72 | .72| .72| .70   | .69| .69|
| 1   | .73    | .72| .73| .72  | .72| .71| .71 | .72| .71| .68   | .67| .67|
| 10  | .73    | .73| .73| .73  | .73| .73| .68 | .69| .69| .66   | .65| .65|
| 100 | .74    | .73| .74| .70  | .71| .71| .66 | .66| .66| .67   | .66| .66|
 

## Decision Trees
The Decision Tree classifier is a non-parametric method that recursively splits the input space into regions based on the features in the dataset. Initially, the random state was set to 0, which led to a low F1-score of 66%.
By increasing the random state to 42 and setting the minimum leaf nodes to 8, the performance improved significantly. This resulted in a precision of 75%, recall of 74%, and an F1-score of 74%. 
The Decision Tree classifier’s performance demonstrated that it can effectively classify individuals with better precision as the SVM classifier. 


## Neural Network
The Neural Network classifier is a powerful machine learning model inspired by the biological neural networks in the brain. It consists of interconnected layers of neurons, where each neuron processes input data and passes it to the next layer. To achieve the best results, various architectures and hyperparameters were experimented.

### Architecture
The best performing architecture consisted of an input layer, followed by three hidden layers with 64, 32 and 16 neurons, respectively. The hidden layers used the rectified linear unit (ReLU) activation function because it helps mitigate the vanishing gradient problem and allows for faster training. A dropout layer with a rate of .20 was added after the second hidden layer to prevent overfitting by randomly turning off 20% of the neurons during training. Finally, the output layer had a single neuron, which returns the probability between 0 and 1, indicating the likelihood of an individual having diabetes. 

The model was compiled using the Adam optimizer with a learning rate of 0.000085. The binary cross-entropy loss function was used, given the binary classification nature of the problem. The model was trained with a batch size of 32 for 100 epochs. 


### Loss and Accuracy
The figure on the left illustrates the relationship between loss and the number of training epochs.
The training loss is plotted in blue, and the validation loss is plotted in orange.
As the number of epochs increases, the training loss shows a consistent decrease, indicating that the model is learning and improving its performance on the training data.
Although the validation loss shows an increase after a certain point, it does not necessarily mean that the model is failing to generalize well.
The increase in the validation loss might be due to the 20% Dropout layer during training or noise in the validation dataset.
This increase in validation loss could also be an indication of overfitting. 
![Accuracy and Loss vs. Epochs](https://raw.githubusercontent.com/domsoos/580/main/Final/ann/loss_and_acc_100_00009.png)

The right figure presents the relationship between accuracy and the number of training epochs.
The training accuracy is plotted in blue, and the validation accuracy plotted in orange.
As the number of epochs increases, both the training accuracy and validation accuracy show consistent increase, indicating that the model is learning and becoming more accurate in its predictions.
The increase in validation accuracy suggests that the model is generalizing well to the unseen data, despite the observed increase in validation loss. 

While the increase in validation loss may raise concerns about overfitting, the concurrent increase in validation accuracy suggests that the model is still generalizing well to the unseen data. It is crucial to consider both loss and accuracy metrics together to get a better understanding of the model’s performance. 

Results and Conclusion
The architecture and training configuration led to a high precision of 78%, recall of 78% and F1-score of 78%, making it the best-performing classifier. The neural network classifier outperformed both the SVM and Decision Tree classifier. The results show the importance of experimenting with different architectures and hyperparameters to find the most suitable solution for a given problem. 


References


https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html









