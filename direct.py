from game import *

#59.3% alone [1500:]
#57.3% alone [1250:]
def m_one(home, away):
	home_val = float(home['RS/G']) - float(home['RA/G'])
	away_val = float(away['RS/G']) - float(away['RA/G'])

	return home_val - away_val

#58.88% at /2
#59.16% at /3
#59.16% at /4
#def m_two(home, away):
#	home_val = float(home['pitcher']['s_ERA'])
#	away_val = float(away['pitcher']['s_ERA'])

	#high number bad
#	return (away_val - home_val) / 4

#57.96% at /4
#def m_two(home, away):
#	home_val = float(home['pitcher']['era'])
#	away_val = float(away['pitcher']['era'])

	#high number bad
#	return (away_val - home_val) / 4

def alg(home, away):
	one = m_one(home, away)
	#two = m_two(home, away)

	return one

#0 home 1 away
def select_winner(val) -> bool:
	if val >= 0:
		return True
	else:
		return False

def all_print_direct(games: list) -> None:
	for game in games:
		try:
			one = Game(game)
			if select_winner(alg(one.home_team, one.away_team)):
				print(one.home_team['name'])
			else:
				print(one.away_team['name'])
		except:
			pass

def one_return_direct(game: Game) -> str:
	try:
		one = Game(game)
		if select_winner(alg(one.home_team, one.away_team)):
			return (one.home_team['name'])
		else:
			return (one.away_team['name'])
	except:
		pass

if __name__ == "__main__":
	#all_print(get_all_game_days())
	print((one_return_direct(get_all_game_days()[0])))