import fresh_tomatoes
import media 

# Movie related information (movie_title, movie_storyline, poster_image,trailer_youtube)

dunkirk = media.Movie("Dunkirk",
					"true story of te Dunkirk evacuations",
					"https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
					"https://www.youtube.com/watch?v=F-eMt3SrfFU")


interstellar = media.Movie("Interstellar",
						"A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival",
						"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
						"https://www.youtube.com/watch?v=zSWdZVtXT7E")

the_dark_knight_rises = media.Movie("The Dark Knight Rises",
								"Batman against the brutal guerilla terrorist Bane",
								"https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
								"https://www.youtube.com/watch?v=g8evyE9TuYk")

the_dark_knight = media.Movie("The Dark Knight",
						"Batman against the sadistic criminal mastermind known as Joker",
						"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
						"https://www.youtube.com/watch?v=kmJLuwP3MbY")

batman_begins = media.Movie("Batman Begins",
						"Batman saves Gotham City from Scarecrow and the League of Shadows",
						"https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
						"https://www.youtube.com/watch?v=neY2xVmOfUM")

inception = media.Movie("Inception",
						"A thief is given the task of planting an idea into the mind of a CEO with the use of dream-sharing technology",
						"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
						"https://www.youtube.com/watch?v=d3A3-zSOBT4")

# movies listed together 
movies = [dunkirk, interstellar, the_dark_knight_rises, inception, the_dark_knight, batman_begins]

#creating movie trailer websites
fresh_tomatoes.open_movies_page(movies)
