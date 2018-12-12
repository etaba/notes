import json
from pprint import pprint
from collections import OrderedDict
TEAMS = { team:id for team,id in zip(['Erick Pirayesh','Dylan Meyer','Tyler Stone','Steve Meyer','Eric Davis','Matt McDonald','Sean  McDonald','Steven Asire','Codey Harrison','Tyler Moore','Jon Fankhauser','luke ceverha','eric taba','jonathan  zerna'],range(1,15))}
TEAMS = { team:id for team,id in zip(['George Matos','eric taba', 'Milind P', 'Craig Chang','John Y','chris lee','DIANE WEAVER','Omar H'],range(1,9))}
TEAMS['Omar H'] = 10


def num_top_7_finish(data):
	results = {t:0 for t in TEAMS}
	for week in range(1,14):
		week = str(week)
		scores = {}
		for team in TEAMS:
			total_score = sum([slot['points'] for slot in data['lineups'][team][week]['lineup']])
			scores[team] = total_score
		for t in sorted([team for team in TEAMS],key=lambda team: scores[team],reverse=True)[:7]:
			results[t] += 1
	ranks = {t:0 for t in TEAMS}
	for i,t in enumerate(sorted([t for t in TEAMS],key=lambda t: results[t],reverse=True)):
		ranks[t] = i + 1
	return ranks

def total_score(data):
	results = {t:0 for t in TEAMS}
	for week in range(1,14):
		week = str(week)
		scores = {}
		for team in TEAMS:
			total_score = sum([slot['points'] for slot in data['lineups'][team][week]['lineup']])
			results[team] += total_score
	ranks = {t:0 for t in TEAMS}
	for i,t in enumerate(sorted([t for t in TEAMS],key=lambda t: results[t],reverse=True)):
		ranks[t] = i + 1
	return ranks


def avg_weekly_score(data):
	results = {t:0 for t in TEAMS}
	for week in range(1,14):
		week = str(week)
		scores = {}
		for team in TEAMS:
			total_score = sum([slot['points'] for slot in data['lineups'][team][week]['lineup']])
			results[team] += total_score
	for t in TEAMS:
		results[t] /= 13
	ranks = {t:0 for t in TEAMS}
	for i,t in enumerate(sorted([t for t in TEAMS],key=lambda t: results[t],reverse=True)):
		ranks[t] = i + 1
	return ranks

def marty_scores(data):
	mj = {}
	TS = total_score(data)
	AWS = avg_weekly_score(data)
	AR = num_top_7_finish(data)
	for t in TEAMS:
		mj[t] = (TS[t] + AWS[t] + AR[t])/3
	return mj


def best_score(roster):
	available = sorted([ (player['player_pos'], player['points']) for player in roster['lineup'] + roster['bench']],key=lambda p: p[1],reverse=True)
	score = 0
	for pos in ['QB','RB','RB','WR','WR','TE','D/ST','K']:
		for i,p in enumerate(available):
			if pos in p[0].split(','):
				if p[1] > 0:
					score += p[1]
				del available[i]
				break
	#flex
	for i,p in enumerate(available):
		if len(set(p[0].split(',')).intersection({'RB','WR','TE'})) > 0:
			if p[1] > 0:
				score += p[1]
			del available[i]
			break
				
	#dp
	for i,p in enumerate(available):
		if len(set(p[0].split(',')).intersection({'LB','S','CB','DE','DT','EDR'})) > 0:
			if p[1] > 0:
				score += p[1]
			del available[i]
			break
	return score



with open('ffl_work_2018.json','r+') as f:
	data = json.load(f)
	
	league_stats = {}
	for team in data['lineups']:
		team_stats = {'total_points_missed':0,'perfect_games':0}
		for week in range(1,14):
			week = str(week)
			actual_score = sum([slot['points'] for slot in data['lineups'][team][week]['lineup']])
			bs = best_score(data['lineups'][team][week])
			if team == 'eric taba':
				print(f'{week} -- {actual_score} -- {bs}')
			team_stats['total_points_missed'] += bs - actual_score
			if bs - actual_score == 0:
				team_stats['perfect_games'] += 1
				print(f'PERFECT: team: {team} week: {week}')
		team_stats['avg_points_missed'] = team_stats['total_points_missed']/13
		league_stats[team] = team_stats

	would_be_records = { team:[0,0] for team in data['lineups'].keys()}
	for week,matchups in data['schedule'].items():
		for away_team,home_team in matchups:
			if best_score(data['lineups'][away_team][week]) > best_score(data['lineups'][home_team][week]):
				would_be_records[away_team][0] += 1
				would_be_records[home_team][1] += 1
			else:
				would_be_records[away_team][1] += 1
				would_be_records[home_team][0] += 1
	print('Average Points Missed')
	for t,p in sorted([(key,stats['avg_points_missed']) for key,stats in league_stats.items()],key=lambda ts:ts[1],reverse=True):
		print(f'{t} -- {p:.2f}')
	print('Would Be Rankings')
	for t,r in sorted(list(would_be_records.items()),key=lambda r:r[1][0],reverse=True):
		print(f'{r[0]}-{r[1]} {t}')

	print('Num top 7 finishes')
	pprint(num_top_7_finish(data))
	print('total scores')
	pprint(total_score(data))
	print('avg scores')
	pprint(avg_weekly_score(data))
	print('MARTY SCORES')
	ms = marty_scores(data)
	for t,s in sorted([(t,s) for t,s in ms.items()],key=lambda ts: ts[1]):
		print(f'{t}: {s:.2f}')

