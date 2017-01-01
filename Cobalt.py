import urllib.request
import requests
from requests.auth import HTTPBasicAuth
import json

#api_key = Ys6AUNnrlKuvIvbK2nxShlMBqKXAJvdJ

def get_decoded_data(url):
    result = urllib.request.urlopen(url).read()
    final_data = json.loads(result.decode())
    return final_data
##
##
##def get_course_info():
##    baseurl = "https://cobalt.qas.im/api/1.0/courses/"
##    #yql_query = "select wind from weather.forecast where woeid=4118"
##    #yql_query = 'select item.condition.text from weather.forecast where woeid in (select woeid from geo.places(1) where text="dallas, tx")'
###    yql_query = 'select item.condition from weather.forecast where woeid = {0}'.format(woeid)
##    yql_url = baseurl + "CSC401H1S20161" + "?key={0}".format(API_KEY)
##    result = urllib.request.urlopen(yql_url).read()
##    info = json.loads(result.decode())
##    return info

def get_exam_data(code, campus):
    url = "https://cobalt.qas.im/api/1.0/exams/filter?q=code:%22{0}%22%20AND%20campus:%22{1}%22&key=Ys6AUNnrlKuvIvbK2nxShlMBqKXAJvdJ".format(code, campus)
    result = urllib.request.urlopen(url).read()
    final_data = json.loads(result.decode())
    return (final_data)

def get_exam_text(code, campus, course=''):
    data = get_exam_data(code, campus)
    for i in range(len(data)):
        if course in data[i]['course_code']:
            print("{0} exam was on {1}".format(data[i]['course_code'], data[i]['date']))

def get_food_data(campus):
    campus = campus.upper()
    url = 'https://cobalt.qas.im/api/1.0/food/filter?q=campus:%22{0}%22&key=Ys6AUNnrlKuvIvbK2nxShlMBqKXAJvdJ'.format(campus)
    data = get_decoded_data(url)
    return data

def get_building_name(building_id, campus):
    url = 'https://cobalt.qas.im/api/1.0/buildings/filter?q=campus:%22{0}%22&key=Ys6AUNnrlKuvIvbK2nxShlMBqKXAJvdJ'.format(campus)
    buil_data = get_decoded_data(url)
    for i in range(len(buil_data)):
        if buil_data[i]['id'] == building_id:
            return buil_data[i]['address']

def get_uoft_food(campus):
    campus = campus.upper()
    data = get_food_data(campus)
    print('Getting Food information for Campus: {0}'.format(campus))
    for i in range(len(data)):
        building = data[i]['address']
        print('{0} at {1}'.format(data[i]['name'], building[0:building.find(',')]))

def what_to_eat(food, campus):
    url = "https://cobalt.qas.im/api/1.0/food/search?q=%22{0}%22%20AND%20campus:%22{1}%22&limit=5&key=Ys6AUNnrlKuvIvbK2nxShlMBqKXAJvdJ".format(food, campus)
    data = get_decoded_data(url)
    print("Getting {0} information for Campus: {1}.format".format(food, campus))
    for i in range(len(data)):
        building = data[
