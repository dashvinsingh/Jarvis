import tmdbsimple as md
md.API_KEY = 'c946883c8e37c6f56a78e54c740191db'


def get_movie_id(name):
    search = md.Search()
    response = search.movie(query = name)
    lst = []
    for s in search.results:
        lst.append(s)
        #print(s['title'])
        return(lst[0]['id'])

def get_movie_name(m_id):
    movie = md.Movies(m_id)
    response = movie.info()
    return movie.title

def get_movie_info(name):
    m_id = get_movie_id(name)
    movie = md.Movies(m_id)
    response = movie.info()
    return response

def get_m_basic_info(name):
    info = get_movie_info(name)
    text = "Movie: {0}\nRuntime: {1} minutes\nRelease Date: {2}\nAverage_Rating: {3}\nOverview: {4}\n"\
           .format(info['original_title'],info['runtime'],info['release_date'], info['vote_average'], info['overview'])
    return print(text)



def get_tv_id(name):
    tv = md.TV()
    search = md.Search()
    response = search.tv(query = name)
    lst = []
    for s in search.results:
        lst.append(s)
        return lst[0]['id']

def get_tv_info(t_id):
    tv = md.TV(t_id)
    response = tv.info()
    return response

def get_tv_overview(t_id):
    return get_tv_info(t_id)['overview']

def get_tv_basic_info(name):
    tv_id = get_tv_id(name)
    info = get_tv_info(tv_id)
    text = "TV Show: {0}\nSeasons: {1}\nEpisodes: {2}\nFirst Air Date: {3}\nOverview: {4}"\
.format(info['name'], info['number_of_seasons'], info['number_of_episodes'],\
        info['first_air_date'], info['overview'])
    return print(text)
    
