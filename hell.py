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

#thought about writing to avoid getting rate limited
#but I still have to use the urls, therefore access the site a lot
#so I guess it does not really help
def write_winners():
	wins = season.findAll("strong")
	f = open("winners21.txt", "a")

	for win in wins[2:len(wins) - 8]:
		f.write(win.text.split("\n")[0].replace(" ", "") + "\n")

	f.close()

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
	print(true_win)
	print(picked_win)
	if true_win.replace(" ", "") == picked_win[0][0].replace(" ", ""):
		return 1
	else:
		return 0

#def find_best_ten(win: list, urls: list):



if __name__ == "__main__":
	#the winners and urls of all games in the 2021 season
	winners = build_winners()[1000:]
	urls = build_urls()[1000:]

	a = Algor(10, 10, 10, 10)
	b = Algor(10, 20, 10, 20)
	c = Algor(10, 30, 10, 5)

	stuff = [a, b, c]
	res = []
	
	for item in stuff:
		count = 0
		for i in range(0, 10):
			if is_correct(winners[i], one_return(item, urls[i])) == 1:
				count += 1

		res.append(count)

	print(res)

