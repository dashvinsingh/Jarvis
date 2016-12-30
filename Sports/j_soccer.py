import urllib.request
import requests
import json
from datetime import *
from difflib import SequenceMatcher

league = 'premier-league'

##def set_league(league):
##    d = list_leagues()['data']['leagues']
##    for item in d:
##        if similar(item['name'], league) > 0.67:
##            league = item['name']
    
def get_decoded_data(url):
    
    result = urllib.request.urlopen(url).read()
    final_data = json.loads(result.decode())
    return final_data

def list_leagues():
    d = get_decoded_data('http://soccer.sportsopendata.net/v1/leagues')['data']['leagues']
    for item in d:
        print("{0} | {1} | {2}".format(item['nation'], item['name'], item['league_slug']))
    
def get_team_names():
    url = 'http://soccer.sportsopendata.net/v1/leagues/{0}/seasons/16-17/teams'.format(league)
    d = get_decoded_data(url)['data']['teams']
    for item in d:
        print(item['name'])

def get_standings():
    url = 'http://soccer.sportsopendata.net/v1/leagues/{0}/seasons/16-17/standings'.format(league)
    d = get_decoded_data(url)['data']['standings']
    print("{0}. {1:>10}  {2:>10}  {3}  {4}  {5}  {6} {7}".format('Position', "Team", 'Played', 'Wins', 'Draws', 'Losses','GD', 'Points'))
    for item in d:
        print("{0}. {1:<20}  {2:>5}  {3:>5}  {4:>5}  {5:>5}  {6:>4} {7:>5}".format(item['position'], item['team'], item['overall']['matches_played'], item['overall']['wins'], item['overall']['draws'], item['overall']['losts'],  item['overall']['goal_difference'], item['overall']['points']))


def extract_name(text):
    lst = []
    for item in text.split():
        if item not in ['team','of', 'what', 'stats', 'score', 'information', 'table', 'form', 'info', 'next', 'game', 'when', 'is', 'the', 'what is']:
            lst.append(item)
    return ' '.join(lst)


def get_team_stats(name):
    url = 'http://soccer.sportsopendata.net/v1/leagues/{0}/seasons/16-17/standings'.format(league)
    dic = get_decoded_data(url)['data']['standings']
    for d in dic:
        if similar(name.title(), d['team']) > 0.67:
            ov = d['overall']
            x = 'Team: {0}\nPosition: {1}\nStats: GP[{5}] W[{2}] L[{3}] D[{4}] GD[{6}]\nPoints: {7}'.format(\
                d['team'], d['position'], ov['wins'], ov['losts'], ov['draws'], ov['matches_played'], ov['goal_difference'], ov['points'])
            return (x)
    return('Invalid Team Name or Team not in English Premier League.')


def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()



def get_team_calendar(team_identifier):
    url = 'http://soccer.sportsopendata.net/v1/leagues/{0}/seasons/16-17/rounds?team_identifier={1}'.format(league, team_identifier)
    result = urllib.request.urlopen(url).read()
    final_data = json.loads(result.decode())
    return final_data

def get_identifier(name):
    url = 'http://soccer.sportsopendata.net/v1/leagues/{0}/seasons/16-17/standings'.format(league)
    d = get_decoded_data(url)['data']['standings']
    for item in d:
        if similar(name.title(), item['team']) > 0.67:
            return item['team_identifier']

def get_name(name):
    url = 'http://soccer.sportsopendata.net/v1/leagues/{0}/seasons/16-17/standings'.format(league)
    d = get_decoded_data(url)['data']['standings']
    for item in d:
        if similar(name.title(), item['team']) > 0.67:
            return item['team']


def next_game(team, days=1):
    d = get_team_calendar(get_identifier(team))['data']['rounds']
#    print(d)
    lst = []
    for item in d:
        if compare_time(item['date_match'][:10]) and len(lst) < days:
            lst.append("{0} vs {1} is going to be played on {2}".format(item['home_team'], item['away_team'], item['date_match'][:10]))
    for item in lst:
        print(item)

def next_game_raw(team, days=1):
    d = get_team_calendar(get_identifier(team))['data']['rounds']
    ng = {}
    count = 1
    for i in range(len(d)):
        if compare_time(d[i]['date_match'][:10]) and len(ng.keys()) < days:
            ng[count] = {'home': d[i]['home_team'], 'away': d[i]['away_team'], 'date': d[i]['date_match'][:10]}
            count += 1
    return ng

def next_game_com(team, days =1):
    d = next_game_raw(team, days)

    for k,v in d.items():
        today = date.today()
        gdate = (v['date'])
        game_day = date(int(gdate[0:4]), int(gdate[5:7]), int(gdate[8:10]))
        countdown = game_day-today
        print("{0} {1:^10}  {2:^5} {3:>5} {4:<5} ({5} days to go)".format(v['home'],'vs', v['away'],'on', v['date'], countdown.days))


def get_score(team1, team2):
    d = get_team_calendar(get_identifier(team1))['data']['rounds']
    team1 = get_name(team1)
    team2 = get_name(team2)
    for item in d:
        if item['home_team'] == team1 and item['away_team'] == team2:
            #print(item['home_team'])
            if item['match_result'] != '':
                return "Final Score: {0} {1} {2}".format(item['home_team'], item['match_result'], item['away_team'])
            else:
                return "This match hasn't started\n{0} vs {1} is going to be played on {2}".format(item['home_team'], item['away_team'], item['date_match'][:10])

    return "This Game is invalid. (Invalid Team Name)"

def get_raw_score(team1, team2):
    d = get_team_calendar(get_identifier(team1))['data']['rounds']
    team1 = get_name(team1)
    team2 = get_name(team2)
    score = {}
    for item in d:
        if item['home_team'] == team1 and item['away_team'] == team2:
            if item['match_result'] != '':
                score[item['home_team']] = item['match_result'][0]
                score[item['away_team']] = item['match_result'][2]
                score['home'] = item['home_team']
                score['away'] = item['away_team']
                score['date'] = item['date_match'][0:10]
                if score[item['home_team']] > score[item['away_team']]:
                    score['winner'] = item['home_team']
                elif score[item['home_team']] == score[item['away_team']]:
                    score['winner'] = "Draw"
                else:
                    score['winner'] = item['away_team']
                return score
            else:
                return "This match hasn't started\n{0} vs {1} is going to be played on {2}".format(item['home_team'], item['away_team'], item['date_match'][:10])
    return "This Game is invalid. (Invalid Team Name)"
                

def extract_t1(text):
    team1 = ''
    text = extract_name(text).split()
    for i in range(len(text)):
        if text[i] in ['versus', 'and', 'vs']:
            team1 = ' '.join(text[0:i])
    return team1

def extract_t2(text):
    team2 = ''
    text = extract_name(text).split()
    for i in range(len(text)):
        if text[i] in ['versus', 'and', 'vs']:
            team2 = ' '.join(text[i+1:])
    return team2

def extract_match_num(text):
    lst = text.split()
    new = []
    for item in lst:
        if (item.lstrip('-').isnumeric()):
            new.append(int(item))
    if len(new) == 0:
        return 1
    else:
        return new[0]

def compare_time(input_d):
    """ str
    Date format = datetime.date(2016, 12, 29)
    date format = 2016-08-13
    """
    today = date.today()
    year = int(input_d[0:4])
    month = int(input_d[5:7])
    day = int(input_d[8:10])
    #print(year, month, day)
    real = date(year, month, day)
    if real >= today:
        return True
    return False
    
