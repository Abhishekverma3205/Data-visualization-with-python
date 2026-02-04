import matplotlib.pyplot as plt
movie_genres = ["comedy","action","thriller","drama"]
genre_counts = [20,35,15,25]
plt.bar(movie_genres, genre_counts)
plt.xticks(range(len(movie_genres)),movie_genres)
plt.yticks(range(0,max(genre_counts)+10,10))
plt.ylabel("number of movies")
plt.title("distribution of movies")
plt.show()