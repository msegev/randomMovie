import requests
import json


class MovieDbApi:
    # useful constant strings
    movieDbApiUrl = 'https://api.themoviedb.org/3/'
    movieDbApiKey = '?api_key=2c9691fb28a58afab362019fda8a2bc9'

    def getAllMovieGenres(self):
        response = requests.get(self.movieDbApiUrl + 'genre/movie/list' + self.movieDbApiKey + '&language=en-US')
        # convert the server response to json object
        genreResponseJson = json.loads(response.text)
        return genreResponseJson

    def getMoviesByGenreId(self, genreId):
        response = requests.get(self.movieDbApiUrl + 'discover/movie' + self.movieDbApiKey + '&with_genres=' + genreId)
        movieResponseJson = json.loads(response.text)
        # print(json.dumps(movieResponseJson, sort_keys=True,indent=4))
        return movieResponseJson

    def getMoviesByGenreIdAndPageNum(self, genreId, pageNum):
        # make a new request to get the results from the randomly selected page
        moviePageRequest = requests.get(self.movieDbApiUrl + 'discover/movie' + self.movieDbApiKey + '&with_genres=' + genreId + '&page=' + str(pageNum))
        moviePageResponseJson = json.loads(moviePageRequest.text)
        # print(json.dumps(moviePageResponseJson, sort_keys=True,indent=4))
        return moviePageResponseJson
