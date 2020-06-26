from sklearn.cluster import KMeans
import numpy as np
import random
import json

###############################################################################
## configuration variables you can modify
###############################################################################

random.seed(0)
num_rows_generated = 1000
player_index = 0
num_clusters = 5

fields = [
    'Number of Components',
    'Delivery Time', 
    'Thread Wait Time', 
    '# of Signals',
    '# of Semaphores'
]

###############################################################################
## Don't modify past here
###############################################################################

def build_entry(values):
    entry = []
    for field_index in range(len(values)):
        row = {}
        row['axis'] = fields[field_index]
        row['value'] = values[field_index]
        entry.append(row)

    return entry

data = []
for _ in range(num_rows_generated):
    data.append([random.random() for _ in range(len(fields))])

cluster_data = []
average_data = []

data = np.array(data)
average_data.append(build_entry(data[player_index]))
average_data.append(build_entry(np.mean(data, axis=0)))

k_means = KMeans(n_clusters=num_clusters, random_state=0).fit(data)
cluster_data = [build_entry(center) for center in k_means.cluster_centers_]

f = open('data.js', 'w')
f.write(f'let userData = {json.dumps(average_data)}\n')
f.write(f'let clusterData = {json.dumps(cluster_data)}')
f.close()