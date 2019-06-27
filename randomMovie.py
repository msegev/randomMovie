from appJar import gui
import requests
import json
import random

#useful constant strings
movieDbApiUrl = 'https://api.themoviedb.org/3/'
movieDbApiKey = '?api_key=2c9691fb28a58afab362019fda8a2bc9'

def getAllMovieGenres():
	response = requests.get(movieDbApiUrl + 'genre/movie/list' + movieDbApiKey + '&language=en-US')
	#convert the server response to json object
	genreResponseJson = json.loads(response.text)
	return genreResponseJson
def getMoviesByGenreId(genreId):
	response = requests.get(movieDbApiUrl + 'discover/movie' + movieDbApiKey + '&with_genres=' + genreId)
	movieResponseJson = json.loads(response.text)			
	#print(json.dumps(movieResponseJson, sort_keys=True,indent=4))
	return movieResponseJson

app=gui("Movie Wizard", "600x200")
app.addLabel("mylabel", "Welcome to Movie Wizard")

#request all the different kind of movie genres
genresJson = getAllMovieGenres()

#create list of genres from json
labelOptions = []
for genre in genresJson["genres"]:
	labelOptions.append(genre["name"]) 

# drop down menu made from list of genres from the moviedb.org
app.setFont(18)
app.addLabelOptionBox("Choose a genre: ", labelOptions)

# go button
genreId = ""

def pressGo(button):
	print("Looking for " + app.getOptionBox("Choose a genre: "))
	#discover movies of the dropdown genre
	
	#todo: make a dictionary of genre name as key and id as value in previous for loop
	for genre in genresJson["genres"]:
		if genre["name"] == app.getOptionBox("Choose a genre: "):
			genreId = str(genre["id"])
			movieResponseJson = getMoviesByGenreId(genreId)
			break

	# choose a random page number
	totalPages = movieResponseJson["total_pages"]
	randomPageNum = random.randrange(1,totalPages,1)

	print("Number of Pages: " + str(totalPages))
	print("Selected Random Page: " + str(randomPageNum))
	
	# make a new request to get the results from the randomly selected page
	moviePageRequest = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=2c9691fb28a58afab362019fda8a2bc9&with_genres=' + genreId + '&page=' + str(randomPageNum))
	moviePageResponseJson = json.loads(moviePageRequest.text)
	#print(json.dumps(moviePageResponseJson, sort_keys=True,indent=4))

	# take a random entry from the results
	resultsLength = len(moviePageResponseJson["results"]) # get length of results
	print("Number of Movie Results on This Page: " + str(resultsLength))

	randomEntry = random.randrange(0,resultsLength-1,1)
	print("Random Entry: " + str(randomEntry))

	print(json.dumps(moviePageResponseJson["results"][randomEntry], sort_keys=True,indent=4))

	# get the title of the randomly selected movie
	movieTitle = moviePageResponseJson["results"][randomEntry]["title"]
	print("Movie title: " + movieTitle)

	# change the label to display movie title
	app.setLabel("movie", movieTitle)


	
app.addButton("Go", pressGo)

app.addLabel("movie", "")

app.go()

print("Goodbye World")
