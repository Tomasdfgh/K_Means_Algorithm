The K Means Algorithm boils down to 3 fundamental steps:

1. Cluster Initialization
2. Cluster Assignment to a specific centroid
3. Move centroid to the center of the cluster

In this project, the first step is done by randomly picking n number of data points if the algorithm calls for n clusters, and assign the coordinates of each of those n clusters to be the same as the coordinate of the n data points. I created a 3D graph containing about 20 data points in 3 dimensions to illustrate the movements of the clusters.


![Initializations](https://user-images.githubusercontent.com/86145397/196065120-e31e875d-97ef-4a68-9029-a77ea212761d.png)

It can be seen that there are three clusters and 3 centroids initialized in this first step. one in the far left and 2 closed together in the middle. All three centroids share the same coordinates as one of the data points.

Step two and three are done in a loop. Data points are being assigned to the closest centroid in step 2 and the centroids will then move towards the center of the data points it is assigned to. Example can be seen below
![Movement](https://user-images.githubusercontent.com/86145397/196065502-de1cfa40-1a0d-4c2f-979a-a245d8b51c59.png)
