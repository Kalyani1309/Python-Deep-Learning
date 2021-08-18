# Assignment-4
Assignment-4

#### Complete the following:

#### Name: Kalyani Nikure
#### Email: kmn6bg@umkc.edu

<br/>

## Video Link: https://www.youtube.com/watch?v=YO11fxOsV20
 
# Assignment-4 Part 1
### Question 1:

![image](https://user-images.githubusercontent.com/30693095/125012545-ff862c00-e02f-11eb-9459-a831495030bf.png)

Accuracy of the existing model provided in the use case file-

![image](https://user-images.githubusercontent.com/30693095/125012179-63f4bb80-e02f-11eb-8996-3824ea465852.png)

I applied the same function to the new model i.e. SVM and calculated the accuracy of the new model. Accuracy of the SVM model is high(~85.31%) compared to the previous model(~77.38%) 

![image](https://user-images.githubusercontent.com/30693095/125012206-70791400-e02f-11eb-8dec-999b7808a4e8.png)

Classification report for SVM using classification_report() function-

![image](https://user-images.githubusercontent.com/30693095/125012231-7bcc3f80-e02f-11eb-8fda-4c8ff2aa1d99.png)

I applied the KNeighborsClassifier model to the same data and accuracy is around 65.78% which is lesser than all the models

![image](https://user-images.githubusercontent.com/30693095/125012263-871f6b00-e02f-11eb-8ad1-d9384a11eff3.png)

Classification report for KNeighborsClassifier using classification_report() function-

![image](https://user-images.githubusercontent.com/30693095/125012286-91416980-e02f-11eb-8853-6f5e9043b94c.png)

Now, I set the tfidf vectorizer parameter to use bigram providing the argument as ngram_range=(1, 2) and train the SVM model.
So the new accuracy is 85.74% which is slightly higher than that of the previously trained model for SVM.

![image](https://user-images.githubusercontent.com/30693095/125012331-9ef6ef00-e02f-11eb-8929-6b5abbff6c57.png)

Set tfidf vectorizer argument to use stop_words='english' and train the SVM model.
So, the new accuracy is 85.10% which is slightly lesser than that of the previously trained model for SVM.

![image](https://user-images.githubusercontent.com/30693095/125012356-addda180-e02f-11eb-8551-fbdc1c276c51.png)

Final Accuracy model accuracies with few changes in the same SVM model-

![image](https://user-images.githubusercontent.com/30693095/125012383-b635dc80-e02f-11eb-905e-54b63b9357bd.png)

</br>

### Question 2:

![image](https://user-images.githubusercontent.com/30693095/125012579-0c0a8480-e030-11eb-98de-78e5bf8d539c.png)

I have read the content from the wiki url provided in the question and extracted the first paragraph to write into the input.txt file.

![image](https://user-images.githubusercontent.com/30693095/125012497-ec735c00-e02f-11eb-9ba8-76908f146899.png)

I have read the contents from the input.txt file and broken it down into sentences using sent_tokenize() function. Sentence Tokenization output is as follow-

![image](https://user-images.githubusercontent.com/30693095/125012764-57249780-e030-11eb-86ba-8bb2376d19d5.png)

We have broken it down into words using word_tokenize() function. Word Tokenization output is as follow-

![image](https://user-images.githubusercontent.com/30693095/125012804-69063a80-e030-11eb-87e1-5149715a0dcc.png)

Part of Speech tagging output using pos_tag() function-

![image](https://user-images.githubusercontent.com/30693095/125012833-73c0cf80-e030-11eb-9973-cce73b78539b.png)

I implemented Stemming for PorterStemmer, LancasterStemmer, SnowballStemmer modules and printed the output-

![image](https://user-images.githubusercontent.com/30693095/125012877-83401880-e030-11eb-846c-c1127202673c.png)

I implimented lemmatization using lemmatize() function on word tokens and below is the output-

![image](https://user-images.githubusercontent.com/30693095/125012904-8dfaad80-e030-11eb-874f-a90af5c83eff.png)

I have printed the Trigram output by first processing it from sentences tokens and looping over to word tokens inside it. Output as below-

![image](https://user-images.githubusercontent.com/30693095/125012931-99e66f80-e030-11eb-96b8-e77780d42871.png)

I extracted Named Entity recognition using the sentences tokens and then using ne_chunk() and pos_tag(), and wordpunct_tokenize() functions on the token. Output as below-

![image](https://user-images.githubusercontent.com/30693095/125012968-a79bf500-e030-11eb-9c66-8dfcffb34369.png)


To find the word counts in the paragrapg, I first applied RegexpTokenizer() function tokenizer to get the words only. Then used dictionary to save the words and it's frequency as key value pair. Dictionary contents are as follows- 

![image](https://user-images.githubusercontent.com/30693095/125012998-b4204d80-e030-11eb-92f5-c3eeccbea540.png)

Below is the plot for Frequencies of words-

![image](https://user-images.githubusercontent.com/30693095/125357254-feedde00-e32c-11eb-80e2-453bc014932b.png)



<br/>
 
# Assignment-4 Part 2
![image](https://user-images.githubusercontent.com/30693095/125012680-3b20f600-e030-11eb-8970-b856e292f49d.png)

Existing model given in the usecase for Diabetes dataset and its accuracy about **67.71%**

![image](https://user-images.githubusercontent.com/30693095/125020164-f69c5700-e03d-11eb-999a-f2e0d84e2768.png)

Summary and Accuracy screenshot for existing model-

![image](https://user-images.githubusercontent.com/30693095/125020185-0320af80-e03e-11eb-83e5-1d75a671ec3a.png)

Added more Dense layers to the existing code with the use of add() function-

![image](https://user-images.githubusercontent.com/30693095/125020209-116ecb80-e03e-11eb-93ee-965b1a5628ea.png)

Added the validation_data=(X_test, Y_test) attribute to .fit() method- 

![image](https://user-images.githubusercontent.com/30693095/125020237-1cc1f700-e03e-11eb-958d-5f4ee5decf48.png)

Summary and Accuracy screenshot for the model with dense parameter added. The Accuracy has increased to **69.79%** than earlier model 1.

![image](https://user-images.githubusercontent.com/30693095/125020273-28adb900-e03e-11eb-9ebc-efc3a03c239c.png)

Plotted the accuracy for training and validation in the same model accuracy plot -

![image](https://user-images.githubusercontent.com/30693095/125020300-35321180-e03e-11eb-9707-fa89f23a9cb4.png)

Normalized the data before feeding the data to the new model and fit it with scaled input data- 

![image](https://user-images.githubusercontent.com/30693095/125020327-42e79700-e03e-11eb-87fe-e651799db921.png)

Accuracy of the model 3 with normalized data. We can see that the accuracy is even more increased than the earlier model. i.e. **72.39%**

![image](https://user-images.githubusercontent.com/30693095/125021395-26e4f500-e040-11eb-8aa9-b25b0b839049.png)



### Breast Cancer Dataset 

Reading the dataset-

![image](https://user-images.githubusercontent.com/30693095/125020468-83471500-e03e-11eb-9711-63e2e59e0b10.png)

Existing model given in the usecase for Diabetes dataset-

![image](https://user-images.githubusercontent.com/30693095/125020510-9528b800-e03e-11eb-90cb-30f5275c9846.png)

Summary and Accuracy screenshot for existing model which is **93.71%**

![image](https://user-images.githubusercontent.com/30693095/125020529-9fe34d00-e03e-11eb-8129-1cadb3d43f03.png)

Added more Dense layers to the existing code with the use of add() function-

![image](https://user-images.githubusercontent.com/30693095/125020557-ad98d280-e03e-11eb-8483-34af0fcb4ec9.png)

Added the validation_data=(X_test, Y_test) attribute to .fit() method- 

![image](https://user-images.githubusercontent.com/30693095/125020576-b7223a80-e03e-11eb-97c9-ff9752a1a699.png)

Summary and Accuracy screenshot for the model with dense parameter added. The Accuracy has changed to **93.00%**

![image](https://user-images.githubusercontent.com/30693095/125020595-c2756600-e03e-11eb-973c-fbc605b1b07b.png)

Plotted the accuracy for training and validation in the same model accuracy plot -

![image](https://user-images.githubusercontent.com/30693095/125020617-cbfece00-e03e-11eb-9642-c6b4ff21e544.png)

Normalized the data before feeding the data to the new model and fit it with scaled input data- 

![image](https://user-images.githubusercontent.com/30693095/125020656-de790780-e03e-11eb-80a6-f7361acc4d57.png)

Accuracy of the model 3 with normalized data. We can see that the accuracy is even more increased than the earlier model. i.e. **95.10%**

![image](https://user-images.githubusercontent.com/30693095/125020686-e9cc3300-e03e-11eb-9cc1-69fb466c61db.png)

**Observation:** We have seen that the model accuracy increased after scaling the data compared to the existing model accuracies.
