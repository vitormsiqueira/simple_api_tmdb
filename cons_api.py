import requests
# pprint is used to format the JSON response
from pprint import pprint

print (' Consulta MOVIES \n')
base_url = 'https://api.themoviedb.org/3/'
api_key = '00fc77df8f735fe4ed9a21dfed246b1d'

id_movie = '155'

movies_details = requests.get(base_url+'movie/'+id_movie+'?api_key='+api_key+'&language=en-US')
print(movies_details.status_code)

print(movies_details.json())