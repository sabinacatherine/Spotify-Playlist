#functions to be used by the Flask routes

#song name stored in song_name variable by the form on the front end

def get_playlist(song_name):
    X = ssf_vectors
    tree = BallTree(X, leaf_size=2)
    ind = tree2.query(X[np.where(pt_concat == song_name)], k = 20)
    playlist = pt_concat.iloc[ind[0]]
    return playlist