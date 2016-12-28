import urllib, json
from urllib.request import urlopen
from urllib.parse import *
import yweather
from os import *
ob = yweather.Client()
import requests
import json

def get_woeid(city):
    try:
        city = city
        woeid = ob.fetch_woeid(city)
        return woeid
    except:
        print('Invalid city name')

def get_weather_yahoo(woeid):
    
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    #yql_query = "select wind from weather.forecast where woeid=4118"
    #yql_query = 'select item.condition.text from weather.forecast where woeid in (select woeid from geo.places(1) where text="dallas, tx")'
    yql_query = 'select item.condition from weather.forecast where woeid = {0}'.format(woeid)
    yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
    result = urllib.request.urlopen(yql_url).read()
    weather_data = json.loads(result.decode())
    return weather_data

def far_to_cel(temp):
    return (float(temp)-32)/1.8

def one_line_weather(city, silent = False):
    woeid = get_woeid(city)
    data = get_weather_yahoo(woeid)
    try:
        temp_f = data['query']['results']['channel']['item']['condition']['temp']
        temp_c = round(far_to_cel(temp_f))
        condition = data['query']['results']['channel']['item']['condition']['text']
        if temp_c >= 0:
            if silent == False:
                print('It is {0}C and {1} outside in {2}'.format(temp_c, condition, city.title()))
                system('say It is {0} degrees celcius and {1} outside in {2}'.format(temp_c, condition, city.title()))
            else:
                print('It is {0}C and {1} outside in {2}'.format(temp_c, condition, city.title()))
        else:
            if silent == False:
                print('It is {0}C and {1} outside in {2}'.format(temp_c, condition, city.title()))
                system('say it is negative {0} degrees celcius and {1} outside in {2}'.format(abs(temp_c), condition, city.title()))
            else:
                print('It is {0}C and {1} outside in {2}'.format(temp_c, condition, city.title()))

    except:
        print('Unable to get weather information, please try again.')

def extract_city(text):
    lst = text.split()
    city_lst = lst[lst.index('in')+1:]
    city_str = " ".join(city_lst)
    return city_str

def current_location():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    return '{0} {1} {2}'.format(j['city'], j['region_name'], j['country_name'])
