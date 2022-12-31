# K Means Algorithm

## Introduction

This project is a python implementation of the k means algorithm, which is data clustering algorithm for unsupervised learning. This article will contain a brief overview of the K means algorithm, a breakdown of the code that I have created, and a discussion of the outcome of the code. In order to have a quicker read, feel free to jump directly to the outcome for discussion of what the code has produced and a visual representation of the algorithm in 2 and 3 dimensions.

## Overview
The overarching goal of the algorithm is to assign the data set into specific clusters (number of clusters is a parameter that the user can decide), and K Means Algorithm boils down to 3 fundamental steps:

1.	Cluster centroids Initialization
2.	Cluster Assignment to a specific centroid
3.	Move centroid to the center of the cluster

There are two ways to initialize the clusters: either clusters can be given random coordinates, or each cluster can start out sharing coordinates with a random data point. Each method has their own pros and cons; however, I have decided to go with sharing coordinates with a random data point due to the fact that in my testing, random initialization can result in cluster centroids left abandoned by the dataset and not update.

Once the cluster centroids have been initialized, each data point will be assigned to the closest cluster centroid. This assignment will be in the form of a constant in a list. For example, let a data set exist with 30 data points and 5 clusters with data point 25 being assigned to cluster 3. This would mean that there will be an array of 30 elements and element 25 will have a value of 2 (0 for centroid 1, so 2 for centroid 3). This process will be repeated until all data points have had a specific centroid assignment.

Once the data points have been assigned to a centroid, each centroid will now calculate the average position of their cluster (all the data points that has been assigned to that centroid) and move to that location. This process will be repeated until every single centroids stop updating after an iteration, signalling that all the centroids have rest in their final position. Step 2 and 3 can be simplified using the loss function for k means algorithm, which is stated as follows

![image](https://user-images.githubusercontent.com/86145397/210133894-3212f3e7-0111-4f71-8ed1-faefdcbac804.png)

Where c’s are centroid assignment constants and µ’s are centroid’s coordinate. In order to minimize this J function, step 1 and 2 can be follows, which is

![image](https://user-images.githubusercontent.com/86145397/210133901-51713198-acf8-41f4-918e-a0f48954516e.png)

Where step 2 is to hold the cluster centroids coordinate fix and step 3 is to hold the centroid’s assignment constant fix. 

## Code

The code for this algorithm simply follows the steps indicated in the overview section, the k means function accepts a data set and the number of centroids as a parameter. Once the function has been called, centroid coordinates are created for the k number of centroids requested. If the data set is in 2 or 3 dimensions, the function will visually demonstrate what the dataset will look like with a 2D or 3D graph. The graph will contain the dataset and all the centroids. Immediately after, the algorithm falls into a loop where step 2 and 3 will be repeated until the centroids' coordinate ceases to update after an iteration. Eventhough this algorithm goes through the entire data set, there will be no stopping requirement based on the number of epochs traversed. The only stopping requirement will be when the centroids stop updating. Once the initial graph is closed, users can see a new graph where the centroids have now relocated to their new location and will eventually converge to their final location.

## Result

### 2D Trial

For the 2D dataset, I created a set of 12 data points that all exist in 2 dimensions. A 2D graph to illustrate the data points and the intial centroids location can be seen below

![F1_2D](https://user-images.githubusercontent.com/86145397/210154302-276c8fdf-7d12-4666-9cb5-c2af20ae34d8.png)

The data points are in blue and the centroids are the red x's. It is obvious that there are 2 clusters and now the objective of the centroids will be to detect the 2 clusters. Step 2 and 3 are now repeated in a loop until the clusters stop updating. The next iterations can be seen below

![F2_2D](https://user-images.githubusercontent.com/86145397/210154486-56ad3c59-609a-4d8c-83f6-c3fe4e7a82b3.png)

Visually, it can be seen that the centroids have begin to migrate towards their clusters. At the next iteration, the centroids will rest in their final destination

![F3_2D](https://user-images.githubusercontent.com/86145397/210154536-120f6ab5-4fcf-4662-84c4-36df7942e210.png)

The algorithm is now terminated and the clusters have clearly been defined.

### 3D Trial

I created a dataset which contains about 20 data points that all exists in 3 dimensions. A 3D graph to illustrate the movements of the clusters can be seen below

![Initializations](https://user-images.githubusercontent.com/86145397/196065120-e31e875d-97ef-4a68-9029-a77ea212761d.png)

It can be seen that there are 3 obvious clusters and 3 centroids (red x's) initialized in this first step. one in the far left and 2 closed together in the middle. All three centroids share the same coordinates as one of the data points.

Step two and three are done in a loop. Data points are being assigned to the closest centroid in step 2 and the centroids will then move towards the center of the data points it is assigned to, which can be seen below

![Movement](https://user-images.githubusercontent.com/86145397/196065502-de1cfa40-1a0d-4c2f-979a-a245d8b51c59.png)

Finally this step will be repeated until the centroids have rested in their final positions and the clusters are clearly being defined. Such as below

![Figure_1](https://user-images.githubusercontent.com/86145397/196065549-f739a94b-60b9-4597-aecf-4939f8e5f766.png)

### Generalized Example (More than 3D)

The example shown previously is only for data points in 3 dimensions. The algorithm that I designed can be generalized up to $n \in R$ dimensions. In another word, datasets can have as many dimensions as neccessary. In the code, I used another data base that holds data for breast cancer patients that has 30 attributes. That means that every single data points has 30 dimensions. I calculated the distortions for 2 centroids up to and including 7 centroids to see how the distortions would change with changing number of centroids. Furthermore, since the dimension of this example is higher than 3, there will be no visual representation of the dataset. Result of the distortions can be seen below

![Distortions vs  Number of Centroids Final Final](https://user-images.githubusercontent.com/86145397/196065777-a6c1c4a9-6f4f-46de-83c2-140232d031db.png)

Using the elbow rule method, I can determine that the correct number of centroids should be 4.
