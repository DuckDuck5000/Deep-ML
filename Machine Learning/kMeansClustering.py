

```
Write a Python function that implements the k-Means algorithm for clustering, starting with specified initial centroids and a set number of iterations. The function should take a list of points (each represented as a tuple of coordinates), an integer k representing the number of clusters to form, a list of initial centroids (each a tuple of coordinates), and an integer representing the maximum number of iterations to perform. The function will iteratively assign each point to the nearest centroid and update the centroids based on the assignments until the centroids do not change significantly, or the maximum number of iterations is reached. The function should return a list of the final centroids of the clusters. Round to the nearest fourth decimal.

Example
Example:
        input: points = [(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)], k = 2, initial_centroids = [(1, 1), (10, 1)], max_iterations = 10
        output: [(1, 2), (10, 2)]
        reasoning: Given the initial centroids and a maximum of 10 iterations,
        the points are clustered around these points, and the centroids are
        updated to the mean of the assigned points, resulting in the final
        centroids which approximate the means of the two clusters.
        The exact number of iterations needed may vary,
        but the process will stop after 10 iterations at most.
```



import numpy as np

'''
Basically cleaned up this guy's code:
https://medium.com/@rishit.dagli/build-k-means-from-scratch-in-python-e46bf68aa875

'''
def euclidean_distance(a, b):
    return np.sqrt(np.sum((np.array(a) - np.array(b)) ** 2))

def k_means_clustering(points, k, initial_centroids, max_iterations):
    centroids = np.array(initial_centroids)
    points = np.array(points)
    
    for iteration in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for point in points:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid_index = np.argmin(distances)
            clusters[closest_centroid_index].append(point)
        
        new_centroids = []
        for cluster in clusters:
            if cluster:  
                new_centroid = np.mean(cluster, axis=0)
            else:
                new_centroid = centroids[len(new_centroids)]  
            new_centroids.append(new_centroid)
        
        new_centroids = np.array(new_centroids)
        
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids
    
    return centroids.tolist()
