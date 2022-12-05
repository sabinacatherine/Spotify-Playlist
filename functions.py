#functions to be used by the Flask routes
#song name (name) stored in song_name variable by the form on the front end

from sklearn.neighbors import BallTree
import numpy as np
import pandas as pd

pt_concat = pd.read_csv("https://github.com/sabinacatherine/Spotify-Playlist/blob/main/data/song_names.csv?raw=true")

def get_playlist(song_name):
    ssf_vectors = np.load("//Users/sabinagrossman/Documents/GitHub/song_vectors.npy")
    X = ssf_vectors
    tree = BallTree(X, leaf_size=2)
    ind = tree.query(X[np.where(pt_concat['SName'] == song_name)], k = 20)
    playlist = pt_concat.iloc[ind[:0]]
    return playlist