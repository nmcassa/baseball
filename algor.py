from game import *

class Algor:
	def __init__(self, w_one: float, w_two: float, w_three: float, w_four: float):
		self.one = w_one
		self.two = w_two
		self.three = w_three
		self.four = w_four

	def m_one(self, team) -> tuple:
		era = float(team['pitcher']['era'])
		ra = float(team["RA/G"])

		return (ra - era, self.one)

	def m_two(self, team) -> tuple:
		rs = float(team['RS/G'])
		ra = float(team['RA/G'])

		return (rs - ra, self.two)

	def m_three(self, team) -> tuple:
		era = float(team['pitcher']['era'])
		sera = float(team['pitcher']['s_ERA'])

		sip = team['pitcher']['s_IP']

		if sip['five'] + sip['seven'] < 20.0:
			return (0, "F")

		#return (era - sera, .5 * (sip['five'] + sip['seven'] * (1.2)))
		return (era - sera, self.three)

	def m_four(self, team) -> tuple:
		sera = float(team['pitcher']['s_ERA'])
		ra = float(team["RA/G"])

		return (ra - sera, self.four)

	def give_me(self, game: Game) -> list:
		h_team = game.home_team
		a_team = game.away_team
		return [self.m_one(h_team)[0], self.m_two(h_team)[0], 
			self.m_three(h_team)[0], self.m_four(h_team)[0],
			self.m_one(a_team)[0], self.m_two(a_team)[0], 
			self.m_three(a_team)[0], self.m_four(a_team)[0]]

	def algor(self, game: Game) -> tuple:
		#home team has a 8.11% advantage, given by historical data

		home = 0
		away = 0

		h_one = self.m_one(game.home_team)
		home += h_one[0] * h_one[1]

		a_one = self.m_one(game.away_team)
		away += a_one[0] * a_one[1]

		h_two = self.m_two(game.home_team)
		home += h_two[0] * h_two[1]

		a_two = self.m_two(game.away_team)
		away += a_two[0] * a_two[1]

		h_three = self.m_three(game.home_team)

		if h_three[0] == "F":
			raise Exception("Filter")
			#return ([game.home_team['name'], "Filter"], [game.away_team['name'], "Filter"])

		home += h_three[0] * h_three[1]

		a_three = self.m_three(game.away_team)
		away += a_three[0] * a_three[1]

		h_four = self.m_four(game.home_team)
		home += h_four[0] * h_four[1]

		a_four = self.m_four(game.away_team)
		away += a_four[0] * a_four[1]

		return ([game.home_team['name'], round(home, 5)], [game.away_team['name'], round(away, 5)])

def all_print(algor, show_json: bool) -> None:
	for game in get_all_game_days():
		one_print(game, show_json)

def one_print(algor, game: Game, show_json: bool) -> None:
	one = Game(game)

	if show_json:
		print(one.jsonify())

	print(algor.algor(one))

def one_return(algor, game: Game) -> None:
	try:
		one = Game(game)
		return algor.algor(one)
	except:
		return "None"

def all_print_difference(algor, games: list) -> None:
	for game in games:
		try:
			one = Game(game)
			sol = algor(one)
		except:
			continue
			print("%s ND %s" % (sol[0][0], sol[1][0]))
		else:
			if sol[0][1] > sol[1][1]:
				print("%s %d" % (sol[0][0], sol[0][1] - sol[1][1]))
			else:
				print("%s %d" % (sol[1][0], sol[1][1] - sol[0][1]))

if __name__ == "__main__":
	#one_print(True)
	#all_print(False)
	#a = Algor(10, 10, 10, 10)
	#print(get_all_game_days())
	#one_print(a, get_all_game_days()[0], False)
	print("he")

