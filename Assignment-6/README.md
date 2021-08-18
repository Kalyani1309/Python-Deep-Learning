# Assignment-6
Assignment-6

#### Complete the following:

#### Name:  Kalyani Nikure
#### Email: kmn6bg@umkc.edu

<br/>

### Video Link: https://www.youtube.com/watch?v=IZBP0vxRjVE

<br/>

## Assignment-6 Part 1

### 1. Follow the instruction below and then report how the performance changed.(apply all at once)

Accuracy of the existing model-

![image](https://user-images.githubusercontent.com/30693095/126733391-91511cc2-a178-4513-b7e0-16d2f81fb337.png)

![image](https://user-images.githubusercontent.com/30693095/126733450-cbe2b21e-d3c1-4c7e-bb31-d2b1744926e5.png)

### 2. Did the performance change?

![image](https://user-images.githubusercontent.com/30693095/126733494-58cbef25-cfd3-4254-b08e-4e851f31ad82.png)


### 3. Change the previous model into Keras Functional API model. 

![image](https://user-images.githubusercontent.com/30693095/126733568-1bbcaa95-4a29-40c1-906d-315ae43f8a89.png)

API Model accuracy- 

![image](https://user-images.githubusercontent.com/30693095/126733611-243d4a2d-5fe0-4351-a74b-58585f769dbf.png)


### 4. Predict the first 4 image of the test data. Then, print the actual label for those 4 images (label means the probability associated with them) to check if the model predicted correctly or not.

![image](https://user-images.githubusercontent.com/30693095/126733653-0cf3bd36-5105-48eb-bbbf-518389ecc502.png)


### 5. Build your own dataset by collecting images from the internet for example:
- Transportation images (Airplanes, Trains, Cars, ..)
- Animals (Cats, Dogs, ..)

I have created a cat and dog dataset downloaded from the internet. 

![image](https://user-images.githubusercontent.com/30693095/126733767-35c3ea3f-f921-40f6-97bf-aee4eb935cfa.png)


![image](https://user-images.githubusercontent.com/30693095/126733737-cbbe8815-a27e-47d8-a7fd-6e7de76a42ef.png)


### 5.1 Train the model on your dataset and report the accuracy.

![image](https://user-images.githubusercontent.com/30693095/126733876-7722a9bd-da49-492b-8b95-cf34c1d38f9b.png)

Model Accuracy for animals data-

![image](https://user-images.githubusercontent.com/30693095/126733899-56e039f8-548e-46d7-827b-d1d8e78b86c7.png)

### 5.2 Plot the training and validation accuracy.

![image](https://user-images.githubusercontent.com/30693095/126733924-8471e6f5-2346-433e-9e75-ec612ad3bc2d.png)

### 6. Apply the following callbacks:
- ModelCheckPoint.
- EarlyStopping.

![image](https://user-images.githubusercontent.com/30693095/126733963-598a8b03-3c5e-4299-9827-d11fb91c62cf.png)

Accuracy after applying ModelCheckPoint and EarlyStopping-

![image](https://user-images.githubusercontent.com/30693095/126733992-d3d400a7-abdc-4eeb-8812-45e5f5f0f191.png)


<br/>

## Assignment-6 Part 2

### 1. Train and save the model and use the saved model to predict on new text data (ex, “A lot of good things are happening. We are respected again throughout the world, and that's a great thing.@realDonaldTrump”)

![image](https://user-images.githubusercontent.com/30693095/126734183-6ad7cf6f-c4aa-4a17-9ff8-8e1888cae2b9.png)


![image](https://user-images.githubusercontent.com/30693095/126734211-f567bb18-f008-4aa7-8d38-ba51c806291c.png)


### 2. Apply the code on spam data set available in the source code (text classification on the spam.csv data set)

![image](https://user-images.githubusercontent.com/30693095/126734241-e90a5632-8abd-443a-a707-97b62f58f012.png)

![image](https://user-images.githubusercontent.com/30693095/126734278-06714b64-fddd-4ff1-871e-6d09824561c7.png)


