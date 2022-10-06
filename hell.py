import re
import requests

from algor import *
from direct import *

from bs4 import BeautifulSoup

season = get_parsed_page("https://www.baseball-reference.com/leagues/majors/2021-schedule.shtml")

def get_parsed_page(url: str) -> None:
	headers = {
		"referer": "https://baseball-reference.com",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
	}

	return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

def build_winners() -> list:
	wins = season.findAll("strong")

	winners = []

	for win in wins[2:len(wins) - 8]:
		winners.append(win.text.split("\n")[0])

	return winners

def build_urls() -> list:
	games = season.findAll("em")

	urls = []

	for game in games:
		try:
			urls.append("/previews/2021/" + game.find("a")['href'][11:])
		except:
			pass

	return urls

def algor_one_prob(winners: list, urls: list, thresh: int) -> float:
	win_count = 0
	lose_count = 0
	nd_count = 0

	for i, game in enumerate(urls):
		winner = ""
		dif = 0
		try:
			sol = one_return(game, False)
			if sol[0][1] > sol[1][1]:
				dif = sol[0][1] - sol[1][1]
				winner = sol[0][0]
			else:
				dif = sol[1][1] - sol[0][1]
				winner = sol[1][0]
			if dif < thresh:
				nd_count += 1
			elif winner.replace(" ", "") == winners[i].replace(" ", ""):
				win_count += 1
				print("%d %d %d" % (win_count, lose_count, win_count / (win_count + lose_count)*100))
			else:
				lose_count += 1
				print("%d %d %d" % (win_count, lose_count, win_count / (win_count + lose_count)*100))
		except:
			nd_count += 1

	return (win_count / (win_count + lose_count))

def algor_direct_prob(winners: list, urls: list) -> float:
	win_count = 0
	lose_count = 0
	nd_count = 0

	for i, game in enumerate(urls):
		winner = ""
		try:
			winner = one_return_direct(game)
			if winner.replace(" ", "") == winners[i].replace(" ", ""):
				win_count += 1
				print("%d %d %d" % (win_count, lose_count, win_count / (win_count + lose_count)*100))
			else:
				lose_count += 1
				print("%d %d %d" % (win_count, lose_count, win_count / (win_count + lose_count)*100))
		except:
			nd_count += 1

	return (win_count / (win_count + lose_count))

if __name__ == "__main__":
	winners = build_winners()[1000:]
	urls = build_urls()[1000:]

	#print(algor_one_prob(winners, urls, 5))
	print(algor_direct_prob(winners, urls))

	