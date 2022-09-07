import re
import requests
import json
from datetime import date
from bs4 import BeautifulSoup
from json import JSONEncoder

class Game: 
	def __init__(self, date: str, home: str) -> None:
		self.home_abb = home
		self.date = date
		self.url = "https://www.baseball-reference.com/previews/2022/" + self.home_abb + self.date + "0.shtml"

		page = self.get_parsed_page(self.url)

		self.away = self.get_away(page)

	def get_parsed_page(self, url: str) -> None:
		headers = {
			"referer": "https://baseball-reference.com",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
		}

		return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

	def jsonify(self) -> str:
		return json.dumps(self, indent=4,cls=Encoder)

	def get_away(self, page: None) -> str:
		data = page.find("h1").text.split(" ")
		self.home = data[1]
		return data[4]

#returns all the teams playing, away team first.
def get_all_game_days() -> list:
	headers = {
		"referer": "https://baseball-reference.com",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
	}

	page = BeautifulSoup(requests.get("https://www.mlb.com/scores", headers=headers).text, "lxml")
	
	games = page.find_all("div", {'data-test-mlb': ['singleGameContainer'], })

	ret = []

	for game in games:
		teams = game.find_all("div", {'class': ['TeamWrappersstyle__MobileTeamWrapper-sc-uqs6qh-1'], })[2:]
		for team in teams:
			ret.append(team.text)

	return ret

def get_date() -> str:
	x = date.today()
	return str(x).replace('-', '')

class Encoder(JSONEncoder):
	def default(self, o):
		return o.__dict__

if __name__ == "__main__":
	today = Game(get_date(), "CLE")
	print(today.jsonify())
	#print(today.away_team)
