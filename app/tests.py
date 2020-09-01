import requests

url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt1375666"

headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "11f73d77e2msh6fa7bccf408b169p14a164jsn27c043803560"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)