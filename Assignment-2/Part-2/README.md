# Assignment2_Part2
Assignment- 2 Part-2: Machine Learning

#### Complete the following:

#### Name: Kalyani Nikure
#### Email: kmn6bg@umkc.edu

<br/>

#### Titanic Dataset
##### Part 1. Find the correlation between ‘survived’ (target column) and ‘sex’ column for the Titanic use case in class. Do you think we should keep this feature?
![image](https://user-images.githubusercontent.com/30693095/122307965-00182080-ced1-11eb-9344-c74f25f94d45.png)
I have found out correlation between 'survived' and 'sex' column using corr() and the value is ~0.543 which is quite significant.

##### Part 2. Do at least two visualizations to plots to describe or show correlations. (e.g.: Survived: Class and gender).
![image](https://user-images.githubusercontent.com/30693095/122307319-b3801580-cecf-11eb-81e3-0e32e67e500e.png)
The plot above shows the pointplot between Survived: 'Pclass' and 'Sex' columns.


![image](https://user-images.githubusercontent.com/30693095/122307353-c4c92200-cecf-11eb-8abe-0893f29f1a2a.png)
The plot above shows the barplot between Survived: 'Pclass' and 'Sex' columns. Bar plot is very efficient in showing the comparative changes in quantity among the survived and non survived values.

</br>

#### Glass Dataset
#### Part 1: Naïve Bayes method 
1. Implement Naïve Bayes method using scikit-learn library.
a. Use the glass dataset available in Link also provided in your assignment.
b. Hold a small percentage of the data set for validation.
c. Use train_test_split to create training and testing part.
![image](https://user-images.githubusercontent.com/30693095/122307542-2b4e4000-ced0-11eb-865f-0fe34869021d.png)
In this, I have first read the dataset and then split it using train_test_split function. 75% of the dataset is training data and 25% data is testing data.

2. Evaluate the model on testing part using score
3. Use the model to Predict the classes of the validation set & mean accuracy.
![image](https://user-images.githubusercontent.com/30693095/122307608-48830e80-ced0-11eb-9212-ff0fbe3d0c7c.png)
Finally, we fit the model using training dataset and predict the values on test dataset. Accuracy is shown as ~46% for Naives Bayes model with the detailed classification report.

#### Part 2: linear SVM method 
1. Implement linear SVM method using scikit library
a. Use the glass dataset available in Link also provided in your assignment.
b. Hold a small percentage of the data set for validation.
c. Use train_test_split to create training and testing part.
![image](https://user-images.githubusercontent.com/30693095/122307749-8ed86d80-ced0-11eb-9024-07848b8c43fa.png)
In this, I have first read the dataset and then split it using train_test_split function. 75% of the dataset is training data and 25% data is testing data.

2. Evaluate the model on testing part using score 
3. Use the model to Predict the classes of the validation set & mean accuracy.
![image](https://user-images.githubusercontent.com/30693095/122307830-ad3e6900-ced0-11eb-8ef6-d5b131b1f6e2.png)
Finally, we fit the model using training dataset and predict the values on test dataset. Accuracy is shown as ~56% for linear SVM model with the detailed classification report.

