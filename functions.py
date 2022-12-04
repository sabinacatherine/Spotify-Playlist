#functions to be used by the Flask routes
#song name (name) stored in song_name variable by the form on the front end

from sklearn.neighbours import BallTree
import numpy as np

def get_playlist(name):
    ssf_vectors = "/Users/sabinagrossman/Documents/GitHub/song_vectors"
    X = ssf_vectors
    tree = BallTree(X, leaf_size=2)
    ind = tree.query(X[np.where('SName' == name)], k = 20)
    playlist = pt_concat.iloc[ind[0]]
    return playlist