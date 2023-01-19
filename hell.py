import re
import requests
import sys
import time

from algor import *
from direct import *

from bs4 import BeautifulSoup

season = get_parsed_page("https://www.baseball-reference.com/leagues/majors/2021-schedule.shtml")

def get_parsed_page(url: str) -> None:
	headers = {
		"referer": "https://baseball-reference.com",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
	}

	sleep(10)

	return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

#1 if home wins 0 if away wins
def build_winners() -> list:
	wins = season.findAll("p", {"class": "game"})

	winners = []

	for win in wins:
		if win.findChildren()[0].name == "strong":
			winners.append(0)
		else:
			winners.append(1)

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

def is_correct(true_win: str, picked_win: str):
	if true_win.replace(" ", "") == picked_win[0][0].replace(" ", ""):
		return 1
	else:
		return 0

if __name__ == "__main__":
	#the winners and urls of all games in the 2021 season
	winners = build_winners()[1000:]
	urls = build_urls()[1000:]

	f = open("data21.csv", "a")

	for cnt, game in enumerate(urls):
		time.sleep(2)
		try:
			one = Game(game)
			attr = give_me_straight(one)
			for item in attr:
				f.write(str(item) + ",")
			f.write(str(winners[cnt]) + "\n")
		except Exception as e:
			print(e)

	#for item in attr:
	#	f.write(str(item) + ",")
	#f.write(str(win) + "\n")

	f.close()


