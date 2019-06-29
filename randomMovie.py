from appJar import gui
import json
import random
from MovieDbApi import MovieDbApi


# go button on press callback
def pressGo(button):
    print("Looking for " + app.getOptionBox("Choose a genre: "))
    # Discover movies of the dropdown genre

    # todo: make a dictionary of genre name as key and id as value in previous for loop
    for genre in genresJson["genres"]:
        if genre["name"] == app.getOptionBox("Choose a genre: "):
            genreId = str(genre["id"])
            movieResponseJson = movieDbApi.getMoviesByGenreId(genreId)
            break

    # choose a random page number
    totalPages = movieResponseJson["total_pages"]
    randomPageNum = random.randrange(1, totalPages, 1)
    print("Number of Pages: " + str(totalPages))
    print("Selected Random Page: " + str(randomPageNum))

    moviePageResponseJson = movieDbApi.getMoviesByGenreIdAndPageNum(genreId, randomPageNum)

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


app = gui("Movie Wizard", "600x200")
app.addLabel("mylabel", "Welcome to Movie Wizard")

# Create Movie DB API object
movieDbApi = MovieDbApi()

# Request all the different kind of movie genres
genresJson = movieDbApi.getAllMovieGenres()

# Create list of genres from json
labelOptions = []
for genre in genresJson["genres"]:
    labelOptions.append(genre["name"])

# drop down menu made from list of genres from the moviedb.org
app.setFont(18)
app.addLabelOptionBox("Choose a genre: ", labelOptions)





app.addButton("Go", pressGo)

app.addLabel("movie", "")

app.go()

print("Goodbye World")
