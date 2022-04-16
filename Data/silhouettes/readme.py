'''Example of Python code reading the silhouette of LAST SUBJECT'''
import numpy as np
loaded = np.load('subject_9.npz')

#get silhouette data of size (n_gait, n_frame, n_height, n_width)
data = loaded['data']

#get a specific silhouette
silh = data[0,0,:,:]

#print information
print(data.shape)
#expected results:
#(9, 1200, 424, 512)
