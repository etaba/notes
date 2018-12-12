from bs4 import BeautifulSoup
import requests
from collections import namedtuple
from pprint import pprint
import json

COOKIES = {'SWID': '{7C03F19F-1221-43BB-83F1-9F122153BB1C}',
           'espn_s2': 'AEBTiswWjOVfrorHvFWhAEuxJBjGcY94cfpHoL702D8SW5bL%2F6emSF5CWvb0uZ7fN1jZH2NAwN6qfqi1FcO5zp2Gm4qBudZwnmuX4BWub1dXLwPXOWPB5axYjNcJLe2QwbA44ZdzqkHlTmtVpwNvs0EQYHxnSxCas0NGAK73UCLIRjY5FTspqG5rUOBDLICaIq91pK1%2FmEYge74YmzUNlQPW7WXI8V%2BqgLqRu8xF0QY7SY8HBudiXaIkBgXXOGduYf7fDLo2SRbwCvxSD8%2F6521j'}

TEAMS = { team:id for team,id in zip(['Erick Pirayesh','Dylan Meyer','Tyler Stone','Steve Meyer','Eric Davis','Matt McDonald','Sean  McDonald','Steven Asire','Codey Harrison','Tyler Moore','Jon Fankhauser','luke ceverha','eric taba','jonathan  zerna'],range(1,15))}
TEAMS = { team:id for team,id in zip(['George Matos','eric taba', 'Milind P', 'Craig Chang','John Y','chris lee','DIANE WEAVER','Omar H'],range(1,9))}
TEAMS['Omar H'] = 10
LEAGUE = '84234'#'977855'



#get schedule:
#schedule = {<int>week: 
#						[Match(away,home)]}
Match = namedtuple('Match','away home')
r = requests.get(f'http://games.espn.com/ffl/schedule?leagueId={LEAGUE}',cookies=COOKIES)
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find('table', class_='tableBody')
schedule = { i:[] for i in range(1,14)}
week = 0
for tr in table.find_all('tr'):
	if tr['bgcolor'] == '#1d7225':
	# if 'class' in tr and 'tableSubHead' in tr['class']:
		week += 1
		if week > 13:
			break
	elif tr['bgcolor'] == '#f2f2e8' or tr['bgcolor'] == '#f8f8f2':
		tds = tr.find_all('td')
		away_team = tds[1].text
		home_team = tds[4].text
		schedule[week].append(Match(away_team,home_team))


#get every team's week breakdown
lineups = { team:{ week:{'lineup':[],'bench':[]} for week in range(1,14)} for team in TEAMS.keys() }
for week in range(1,14):
	for team in TEAMS.keys():
		url = f'http://games.espn.com/ffl/boxscorequick?leagueId={LEAGUE}&teamId={TEAMS[team]}&scoringPeriodId={week}&seasonId=2018&view=scoringperiod&version=quick'
		r = requests.get(url,cookies=COOKIES)
		soup = BeautifulSoup(r.content, 'html.parser')
		#get lineup
		table = soup.find('table', id='playertable_0')
		for tr in table.find_all('tr',class_='pncPlayerRow'):
			tds = tr.find_all('td')
			slot = tds[0].text
			try:
				player = tds[1].find('a').text
				player_info = tds[1].find(text=True,recursive=False)
				if 'D/ST' in player_info:
					player_pos = 'D/ST'
				else:
					player_pos = ''.join(player_info.split()[2:])
				if len(tds) == 5:
					points = float(tds[4].text) if tds[4].text != '--' else 0
				else:
					points = float(tds[3].text) if tds[3].text != '--' else 0
			except Exception:
				player = ''
				player_pos = ''
				points = 0
			lineups[team][week]['lineup'].append({'slot':slot,'player':player,'player_pos':player_pos,'points':points})
		#get bench
		table = soup.find('table', id='playertable_1')
		for tr in table.find_all('tr',class_='pncPlayerRow'):
			tds = tr.find_all('td')
			try:
				player = tds[1].find('a').text
				player_info = tds[1].find(text=True,recursive=False)
				if 'D/ST' in player_info:
					player_pos = 'D/ST'
				else:
					player_pos = ''.join(player_info.split()[2:])
				if len(tds) == 5:
					points = float(tds[4].text) if tds[4].text != '--' else 0
				else:
					points = float(tds[3].text) if tds[3].text != '--' else 0
				lineups[team][week]['bench'].append({'slot':slot,'player':player,'player_pos':player_pos,'points':points})
			except Exception:
				pass
with open('ffl_work_2018.json','w+') as f:
	json.dump({'schedule':schedule,'lineups':lineups},f)