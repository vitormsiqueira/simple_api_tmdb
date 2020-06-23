import requests
# pprint is used to format the JSON response
from pprint import pprint

print (' Consulta MOVIES \n')
base_url = 'https://api.themoviedb.org/3/'
api_key = '00fc77df8f735fe4ed9a21dfed246b1d'

id_movie = '155'


# Get the primary information about a movie.
def get_overview_movie(base_url, api_key, id_movie): 

    movies_details = requests.get(base_url+'movie/'+id_movie+'?api_key='+api_key+'&language=en-US')

    if movies_details.status_code != 200:
        print('Ocorreu um erro na solicitação')
        exit()
    else:
        # converte o response em json
        m_d = movies_details.json()

        # salva o overview do filme
        overview = 'overview : {}'.format(m_d['overview'])

        return overview


# Get the top rated movies on TMDb.
def get_top_rated_movies(base_url, api_key): 

    arr_top_rated_movies = []

    top_rated_movies = requests.get(base_url+'movie/top_rated?api_key={}&language=en-US&page=1/'.format(api_key))

    if top_rated_movies.status_code != 200:
        print('Ocorreu um erro na solicitação')
        exit()
    else:
        # converte o response em json
        m_d = top_rated_movies.json()

        # acessa o campo results e retorna os titles da lista de results
        for resultado in m_d.get('results'):
            arr_top_rated_movies.append(resultado['title'])
            
    return arr_top_rated_movies


# Get the keywords that have been added to a movie.
def keywords_from_movie(base_url, api_key, movie_id):
    arr_name_keywords = []

    keywords_movie = requests.get(base_url+'movie/'+movie_id+"/keywords?api_key={}".format(api_key))

    if keywords_movie.status_code != 200:
        print('Ocorreu um erro na solicitação')
        exit()
    else:
        # converte o response em json
        m_d = keywords_movie.json()

        for resultado in m_d.get('keywords'):
            arr_name_keywords.append(resultado['name'])

        return arr_name_keywords

# Query the keyword name
def keywords_name(base_url, api_key, id_keyword):

    keywords = requests.get(base_url+'keyword/'+id_keyword+'?api_key={}'.format(api_key))

    if keywords.status_code != 200:
        print('Ocorreu um erro na solicitação')
        exit()
    else:
        # converte o response em json
        m_d = keywords.json()

       # salva a keyword
        keyword_name = 'name : {}'.format(m_d['name'])

        return keyword_name


###########################################################################################


# pprint(get_overview_movie(base_url, api_key, id_movie))

# pprint(get_top_rated_movies(base_url, api_key))

# pprint(keywords_from_movie(base_url, api_key, '155'))

pprint(keywords_name(base_url, api_key, '1308'))