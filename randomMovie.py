from appJar import gui
import requests
import json
import random

#r1 = requests.get('https://api.themoviedb.org/3/search/movie?api_key=2c9691fb28a58afab362019fda8a2bc9&query=fight+club')
#x1 = json.loads(r1.text)
#print(json.dumps(x1, sort_keys=True,indent=4))

#request all the different kind of movie genres
r2 = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=2c9691fb28a58afab362019fda8a2bc9&language=en-US')
x2 = json.loads(r2.text) #convert the server response to json object
#print(json.dumps(x2, sort_keys=True,indent=4))
labelOptions = []
for each in x2["genres"]:
	labelOptions.append(each["name"]) #create list of genres from json

app=gui("Movie Wizard", "600x200")


app.addLabel("mylabel", "Welcome to Movie Wizard")
# app.setLabelBg("mylabel", "blue")
app.setFont(18)

# drop down menu made from list of genres from the moviedb.org
app.addLabelOptionBox("Choose a genre: ", labelOptions)
# go button

genreId = ""

def pressGo(button):
	print("Looking for " + app.getOptionBox("Choose a genre: "))
	#discover movies of the dropdown genre
	 #convert the server response to json object
	
	for each in x2["genres"]:
		if each["name"] == app.getOptionBox("Choose a genre: "):
			genreId = str(each["id"])
			r3 = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=2c9691fb28a58afab362019fda8a2bc9&with_genres=' + genreId)
			x3 = json.loads(r3.text)			
			#print(json.dumps(x3, sort_keys=True,indent=4))
			break

	# choose a random page number
	totalPages = x3["total_pages"]
	randomPageNum = random.randrange(1,totalPages,1)
	
	# make a new request to get the results from the randomly selected page
	r4 = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=2c9691fb28a58afab362019fda8a2bc9&with_genres=' + genreId + '&page=' + str(randomPageNum))
	x4 = json.loads(r4.text)
	print(json.dumps(x4, sort_keys=True,indent=4))

	# take a random entry from the results
	resultsLength = len(x4["results"]) # get length of results
	print("Results length: " + str(resultsLength))

	randomEntry = random.randrange(0,resultsLength-1,1)
	print("Random Entry: " + str(randomEntry))

	print(json.dumps(x4["results"][randomEntry], sort_keys=True,indent=4))

	# get the title of the randomly selected movie
	movieTitle = x4["results"][randomEntry]["title"]
	print("Movie title: " + movieTitle)

	# change the label to display movie title
	app.setLabel("movie", movieTitle)


	
app.addButton("Go", pressGo)

app.addLabel("movie", "")

app.go()

print("Goodbye World")
