# Assignment 3
Week_3 Assignment 3

#### Complete the following:

#### Name: Kalyani Nikure
#### Email: kmn6bg@umkc.edu

<br/>

### Video link: https://www.youtube.com/watch?v=1ljXVz1THIQ&t=13s

### Assignment Part 1
![image](https://user-images.githubusercontent.com/30693095/123328691-8354fa00-d501-11eb-9c9c-3253c1f3025c.png)
#### For Question 1: 
To remove all the outliers from the GarageArea field, I have used F-score method to remove outliers.

Below is the scatterplot before removing outliers-
![image](https://user-images.githubusercontent.com/30693095/123340905-a76d0700-d512-11eb-9fa8-a18b45c8e090.png)

Scatterplot after removing the outliers-
![image](https://user-images.githubusercontent.com/30693095/123340998-d3888800-d512-11eb-9925-717f0f18058b.png)

I created a linear regression model using GarageArea and SalePrice as target variable.
![image](https://user-images.githubusercontent.com/30693095/123341203-311cd480-d513-11eb-8bbe-74281f8c3b21.png)

Model Evaluation values are as follows-

![image](https://user-images.githubusercontent.com/30693095/123341257-4a258580-d513-11eb-9009-4bb4fc275d90.png)

Plotting the regression line-

![image](https://user-images.githubusercontent.com/30693095/123341322-6295a000-d513-11eb-94c9-f675942529ac.png)


#### For Question 2:

I built a multiple linear regression model with all the features considered with target variable as 'revenue'.
Finally, I calculate the RMSE and R^2 value for the model.
![image](https://user-images.githubusercontent.com/30693095/123354569-9085df00-d529-11eb-8f49-b7c0f7384e78.png)

#### For Question 3:

The top 5 most correlated features from the dataset using corr() function-
![image](https://user-images.githubusercontent.com/30693095/123354607-a3001880-d529-11eb-9677-7a26a18bb981.png)

Calculated the RMSE and R^2 value for the model.
![image](https://user-images.githubusercontent.com/30693095/123354647-ac898080-d529-11eb-9e3a-32995f58078b.png)
So, after comparing the RMSE and R^2 values for both the models, top 5 feature model performed better than first model.
It has low RSME value and higher R^2 value which proves a better fit.

<br/>
 
### Assignment Part 2
![image](https://user-images.githubusercontent.com/30693095/123328758-98318d80-d501-11eb-856c-78342b33404b.png)

#### For Question 1:

We apply k-Means clustering on credit card dataset, first staring with loading the data, data pre-processing steps.
Removed any null values by mean-
![image](https://user-images.githubusercontent.com/30693095/123360048-c4193700-d532-11eb-809d-142e45544239.png)

Use the elbow method to find a good number of clusters with the K-Means algorithm-
![image](https://user-images.githubusercontent.com/30693095/123360444-f0cd4e80-d532-11eb-9692-463c2a3f9318.png)

After we receive elbow point as 3, we perform k-Means with k=3 and calculate the Silhouette score.
![image](https://user-images.githubusercontent.com/30693095/123360573-283bfb00-d533-11eb-98f0-a9d8076fe654.png)


#### For Question 2:
We first perform feature scaling on the data. Find the good value of k using elbow method-
![image](https://user-images.githubusercontent.com/30693095/123360790-87017480-d533-11eb-907b-e0af2a66489f.png)

After we receive elbow point as 4, we perform k-Means with k=4 and calculate the Silhouette score.
![image](https://user-images.githubusercontent.com/30693095/123360855-9f718f00-d533-11eb-907d-03b7afec5172.png)

We see that the Silhouette Score is not improved after feature scaling because the features scaling were not required for this dataset. We should do feature scaling when the scale of a feature is irrelevant or misleading, and not do it when the scale is meaningful.


#### For Question 3: PCA

k-Means algorithm after performing PCA-
![image](https://user-images.githubusercontent.com/30693095/123360993-df387680-d533-11eb-9202-a06b249f0c7e.png)

Silhouette Score after K-Means algorithm on the PCA result -
![image](https://user-images.githubusercontent.com/30693095/123361016-ea8ba200-d533-11eb-952e-1c095f051aed.png)

We can see that the Silhouette score has improved from 0.2167 to 0.4533 after performing k-Means algorithm on the PCA result.

Visualization 1: Scatterplot to show k-means clustering (no of clusters =3)
Black points represent the centroid of the clusters
![image](https://user-images.githubusercontent.com/30693095/123361049-fc6d4500-d533-11eb-93a4-aed594f88209.png)

Visualization 2: Two component PCA Graph- 
![image](https://user-images.githubusercontent.com/30693095/123361095-10b14200-d534-11eb-94e4-20449c55eeeb.png)
