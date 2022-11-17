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


if __name__ == "__main__":
	winners = build_winners()[1000:]
	urls = build_urls()[1000:]

	a = Algor(10, 10, 10, 10)
	print(urls[0])
	one_print(a, urls[0], False)

	#print(algor_one_prob(winners, urls, 5))
	#print(algor_direct_prob(winners, urls))

	