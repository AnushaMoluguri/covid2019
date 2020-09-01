



import json
from MoviesApi.settings import MOVIES_API_FILE

class MovieapiMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        fetchMovie_id()
        import requests
        #for title in t_list[1:40]:

        url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"

        headers = {
                'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
                'x-rapidapi-key': "0ac662495cmsha3ddbe01a85b038p1b0e32jsn0541b2f89aff"
            }

        response = requests.request("GET", url, headers=headers)

        dict_data = json.loads(response.text)

        #with open(MOVIES_API_FILE, 'w') as file:
        json.dump(dict_data,open(MOVIES_API_FILE, 'w'), indent=2)

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response

def fetchMovie_id():
    import requests

    url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

    querystring = {"genre": "%2Fchart%2Fpopular%2Fgenre%2Fadventure"}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "0ac662495cmsha3ddbe01a85b038p1b0e32jsn0541b2f89aff"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    resstr=response.text.split('/')
    print(type(resstr))
    l=[]
    for x in resstr:
        if x.split('/'):
            if x.startswith('tt'):
                l.append(x)
    return l
