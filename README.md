# Spotify-Playlist-Creation

## Introduction
In this project, I will create playlists according to numeric and lyrical similarities. Ultimately, I am looking to create the best possible combination of my favourite characteristics and languages and explore some new tunes!

## Packages used
For this project I used the following Python modules for model creation and deployment:
- Numpy
- Matplotlib
- Spotipy
- Sklearn
- Flask (incl. bootstrap, wtforms)
- Pandas
- Fasttext

## Strategy

To aggregate my song data, I knew that I would need to apply a machine learning method to predict similarities between data points. I opted for KMeans here because it scales well, computes quickly and can easily adapt to new examples. Before doing so, I used the FastText language recognition model to vectorize the song lyrics so that KMeans would be able to interpret the words. Once this was done, I tried out a KMeans model with just numerical data, just lyrical data, and both:

![](https://github.com/sabinacatherine/Spotify-Playlist/blob/main/images/Screen%20Shot%202022-12-05%20at%2010.19.00%20AM.png)

I then built a BallTree model to calculate nearest neighbours in the feature matrix:

![](https://github.com/sabinacatherine/Spotify-Playlist/blob/main/images/Screen%20Shot%202022-12-05%20at%2010.32.24%20AM.png)

## Deployment
I deployed my model as an interactive web form which returns a list of songs. We can see an example of it in action here:
![](https://github.com/sabinacatherine/Spotify-Playlist/blob/main/images/Screen%20Shot%202022-12-05%20at%2010.33.59%20AM.png)
![](https://github.com/sabinacatherine/Spotify-Playlist/blob/main/images/Screen%20Shot%202022-12-05%20at%2010.35.01%20AM.png)

## Next steps
As next steps I would like to improve on the indexing function for the Flask app, as I have encountered some indexing issues that were not present in the workbook alone. I would also like to round out the integration with the Spotify API.