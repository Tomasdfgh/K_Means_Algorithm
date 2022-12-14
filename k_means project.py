from sklearn.datasets import load_breast_cancer
import numpy as np
from matplotlib import pyplot as plt

def k_means(data,k):

	#---Initialization---#
	# Cluster centroids placement are picked at a data point


	cens_cord = []
	ran_lst = []
	while len(set(ran_lst)) < k:
		num = np.random.randint(0,len(data))
		ran_lst.append(num)
	ran_lst = set(ran_lst)
	
	for i in range(0,k):
		cens_cord.append(data[ran_lst.pop()])

	print(cens_cord)
	#---End of Initialization---#

	#---Testing Code for 2D---#
	if len(data[0]) == 2:
		x_array = []
		y_array = []
		for i in range(len(data)):
			x_array.append(data[i][0])
			y_array.append(data[i][1])
		clusters_x = []
		clusters_y = []
		for i in range(len(cens_cord)):
			clusters_x.append(cens_cord[i][0])
			clusters_y.append(cens_cord[i][1])
		plt.plot(x_array,y_array,".",clusters_x,clusters_y,"ob")
		plt.show()
	#---End of Testing Code for 2D---#

	#---Testing Code for 3D---#
	if len(data[0]) == 3:
		x_array = []
		y_array = []
		z_array = []
		for i in range(len(data)):
		 	x_array.append(data[i][0])
		 	y_array.append(data[i][1])
		 	z_array.append(data[i][2])
		clusters_x = []
		clusters_y = []
		clusters_z = []
		for i in range(len(cens_cord)):
			clusters_x.append(cens_cord[i][0])
			clusters_y.append(cens_cord[i][1])
			clusters_z.append(cens_cord[i][2])
		fig = plt.figure(figsize = (7,7))
		ax = fig.add_subplot(111,projection = '3d')
		ax.scatter(x_array, y_array, z_array, label = "data")
		ax.scatter(clusters_x,clusters_y,clusters_z,marker = "x", c = "red",label = "centroids")
		plt.show()
	#---End of Testing Code for 3D---#



	#Repeating loop
	stor_cord = []
	temporary = []
	for i in range(len(cens_cord)):
		for z in range(len(cens_cord[0])):
			temporary.append(cens_cord[i][z])
		stor_cord.append(temporary)
		temporary = []
	#print("Stor: " + str(stor_cord))

	while True:
		cen_closest = []
		dist = []
		dist_2 = []
		temp = []
		sum_0 = 0

		#---Cluster Assignment Step---#

		for d in range(0,k):
			for i in range(len(data)): #569
				for z in range(len(data[i])): #30
					sum_0 += (data[i][z] - cens_cord[d][z]) ** 2
				dist.append(np.sqrt(sum_0))
				sum_0 = 0

		for i in range(0,k):
			for z in range(len(data)):
				temp.append(dist.pop(0))
			dist_2.append(temp)
			temp = []


		for i in range(len(data)):
			cen_closest.append(find_least(dist_2,i))

		#---End of Cluster Assignment---#

		#---Move Centroid---#

		mean = []
		for i in range(len(data[0])):
			mean.append(0)

		mean_counter = 0
		for i in range(0,k):
			q = 0
			while q < len(data):
				if cen_closest[q] == i:
					mean_counter += 1
					for p in range(len(data[0])):
						mean[p] += data[q][p]
				q += 1
			if mean_counter != 0:
				for o in range(len(data[0])):
					mean[o] = float(mean[o])/mean_counter
				cens_cord[i] = mean
				mean = []
				for l in range(len(data[0])):
					mean.append(0)
				mean_counter = 0

		#--- End of Move Centroid---#

		#---Testing Code---#
		if len(data[0]) == 2:
			clusters_x = []
			clusters_y = []
			for i in range(len(cens_cord)):
				clusters_x.append(cens_cord[i][0])
				clusters_y.append(cens_cord[i][1])
			plt.plot(x_array,y_array,".",clusters_x,clusters_y,"ob")
			plt.show()
		#---End of Testing Code---#

		#---Testing Code for 3D---#
		if len(data[0]) == 3:
			clusters_x = []
			clusters_y = []
			clusters_z = []
			for i in range(len(cens_cord)):
				clusters_x.append(cens_cord[i][0])
				clusters_y.append(cens_cord[i][1])
				clusters_z.append(cens_cord[i][2])
			fig = plt.figure(figsize = (7,7))
			ax = fig.add_subplot(111,projection = '3d')
			ax.scatter(x_array, y_array, z_array, label = "data")
			ax.scatter(clusters_x,clusters_y,clusters_z,marker = "x", c = "red",label = "centroids")
			plt.show()
		#---End of Testing Code for 3D---#

		#---Terminating Conditions---#
		if cens_cord == stor_cord:
			return cens_cord,cen_closest
		else:
			temporary = []
			stor_cord = []
			for i in range(len(cens_cord)):
				for z in range(len(cens_cord[0])):
					temporary.append(cens_cord[i][z])
				stor_cord.append(temporary)
				temporary = []

		#---End of Terminating Conditions---#
		


def find_max(data, i):
	#i is the index of row
	#this function is to find the max for the specified row
	max_1 = 0
	for z in range(len(data)):
		if data[z][i] > max_1:
			max_1 = data[z][i]
	return max_1

def find_least(dist,i):
	lst = []
	for z in range(len(dist)):
		lst.append(dist[z][i])
	return lst.index(min(lst))

if __name__ == '__main__':
	data = load_breast_cancer()
	data_2c = [[1,3],[2,4],[3,2],[4,1],[5,2],[3,5],[30,15],[31,14],[33,17],[31,12],[35,16],[32,15]]
	data_3c = [[1,3],[2,4],[3,2],[4,1],[5,2],[3,5],[30,15],[31,14],[33,17],[31,12],[35,16],[32,15],[9,30],[12,27],[8,29],[10,26],[6,31],[9,25]]
	data_3c_3d = [[1, 1, 1], [1, 2, 1], [2, 1, 2], [-1, 2, -3], [-2, 2, 1], [0, 0, 0],[34, 56, 1], [29, 54, 3], [33, 58, 3], [30, 50, -1], [33, 59, -4], [31, 52, 2],[-62, -53, 30], [-59, -56, 31], [-60, -60, 34], [-55, -59, 29], [-57, -66, 25], [-50, -61, 32]]

	cens_coord = 0
	cens_index = 0
	x_axis = []
	y_axis = []

	for i in range(2,8):

		cens_coord,cens_index = k_means(data.data,i)
		x_axis.append(i)
		dist_s = 0
		distortions = 0
		for z in range(0,i):
			dist_s = 0
			q = 0
			while q < len(data.data):
				if cens_index[q] == z:
					for s in range(len(data.data[0])):
						dist_s += (data.data[q][s] - cens_coord[z][s])**2
					distortions += dist_s
				q += 1
		distortions = distortions/len(data.data)
		y_axis.append(distortions)




	plt.plot(x_axis,y_axis,"o")
	plt.title("Distortions vs. Number of Centroids")
	plt.xlabel("Number of Centroids (k)")
	plt.ylabel("Distortions")
	plt.show()

