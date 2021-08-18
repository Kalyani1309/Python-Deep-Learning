# Assignment-5
Assignment-5
<br/>
** Part-2 Dataset available in your Canvas assignment file **
<br/>
#### Complete the following:

#### Name: Kalyani Nikure 
#### Email: kmn6bg@umkc.edu

<br/>

## Video Link: https://youtu.be/uTRqVGzFFkI

<br/>

## Assignment-5 Part 1
1. We had used 2 hidden layers and relu activation. Change the number of hidden layers and the activation to tanh or sigmoid and report what happens.

Existing model accuracy -

![image](https://user-images.githubusercontent.com/30693095/126050118-8717851a-8e5b-40c0-98b4-bbc873adf748.png)

![image](https://user-images.githubusercontent.com/30693095/126050129-3d6ea240-9408-4536-a54f-511cc94b39cb.png)

![image](https://user-images.githubusercontent.com/30693095/126050138-d99cd228-2e73-486b-8af5-1993463f5dd0.png)

<br/>

2. Using the history object in the source code, plot the loss and accuracy for both training data and validation data.
Plot for Model Accuracy:

![image](https://user-images.githubusercontent.com/30693095/126050148-0f65a164-fdea-46e5-9271-c84c4e451ffe.png)

Plot for Model Loss:

![image](https://user-images.githubusercontent.com/30693095/126050158-68c9f85d-d40a-4b1e-acd8-f735e74f8cc4.png)

<br/>

3. Plot one of the images in the test data, and then do inferencing to check what is the prediction of the model on that single image in the test data.

![image](https://user-images.githubusercontent.com/30693095/126050166-6da7404b-fb85-4d93-9586-79994d5ceb3b.png)

<br/>

4. Convert the sequential model to API model.

![image](https://user-images.githubusercontent.com/30693095/126050173-8214b6c5-f376-4ceb-b8eb-eb6c309fc111.png)

![image](https://user-images.githubusercontent.com/30693095/126050177-f68b8132-da8d-4926-87bf-c35a0da5ff6d.png)

<br/>

5. Run the same code without scaling the images, how the accuracy changes?

![image](https://user-images.githubusercontent.com/30693095/126050188-4525aa76-a6e7-4b9e-8dc7-6733b50b06a8.png)

<br/>

## Assignment-5 Part 2
1. In the code provided there are three mistake which stops the code from running successfully. Find those mistakes and explain why they need to be corrected to be able to get the code run.

  ![image](https://user-images.githubusercontent.com/30693095/126050242-9e169f03-ee8a-492c-b4f3-c9e1207c7fea.png)

Existing model accuracy:

  ![image](https://user-images.githubusercontent.com/30693095/126050261-4587fcc9-52fe-4ad3-9534-6f35708e18bc.png)

<br/>

2. Add embedding layer to the model, did you experience any improvement?

We pre-process the data before embedding-

![image](https://user-images.githubusercontent.com/30693095/126050286-b278ea08-00c4-4de2-bc56-9107b47602d0.png)

Adding embedding layers to the model-

![image](https://user-images.githubusercontent.com/30693095/126050277-5934b013-19a6-4fea-b3bf-76f332cbef98.png)

Embedded model accuracy -

![image](https://user-images.githubusercontent.com/30693095/126050334-d712da9b-529f-4e3c-a366-982e61dcc23f.png)

<br/>

3. Apply the code on 20_newsgroup data set we worked in the previous classes.

![image](https://user-images.githubusercontent.com/30693095/126050299-42b83bf0-c443-4ee5-9428-6ef00b37d6c2.png)

![image](https://user-images.githubusercontent.com/30693095/126050307-43ad7221-a8b3-4100-add8-62534771817b.png)

![image](https://user-images.githubusercontent.com/30693095/126050310-554bcb47-ded5-4d4d-a13f-d35832576af9.png)

<br/>

4. Plot the loss and accuracy using history object.

![image](https://user-images.githubusercontent.com/30693095/126050341-56337b4d-97b6-444e-8405-123346493c46.png)

![image](https://user-images.githubusercontent.com/30693095/126050350-7ad31f28-cdac-4f86-89d8-4e678c875351.png)

<br/>

5. Predict over one sample of data and check what will be the prediction for that.

![image](https://user-images.githubusercontent.com/30693095/126050355-ca2ad325-5940-4ac6-a699-90dd0d16c283.png)


<br/>

6. BONUS POINT(5): Plot loss and accuracy in Tensorboard.

![image](https://user-images.githubusercontent.com/30693095/126050369-e096f7b7-d8ef-4d06-b428-bc2a39f0ad3a.png)

![image](https://user-images.githubusercontent.com/30693095/126050375-74d75636-dbaa-4d51-b7a3-03b80fecaedf.png)

<br/>

