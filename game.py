import re
import requests
import json
from datetime import date
from bs4 import BeautifulSoup
from json import JSONEncoder

class Game: 
	def __init__(self, url: str) -> None:
		self.url = url
		page = get_parsed_page("https://www.baseball-reference.com" + self.url)

		self.build(page)

	def build(self, page: None) -> None:
		self.get_teams(page)

	def get_teams(self, page: None) -> None:
		data = page.findAll("h2")
		self.home_team = data[0].text
		self.home_abb = data[1].text.split(" ")[0]
		self.away_team = data[3].text
		self.away_abb = data[4].text.split(" ")[0]

	def jsonify(self) -> str:
		return json.dumps(self, indent=4,cls=Encoder)

def get_parsed_page(url: str) -> None:
	headers = {
		"referer": "https://baseball-reference.com",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
	}

	return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

#returns all the urls previews for all the days games
def get_all_game_days() -> list:
	page = get_parsed_page("https://www.baseball-reference.com/previews/")
	data = page.findAll("a", text = "Preview")

	urls = []

	for data_point in data:
		urls.append(data_point['href'])

	return urls

class Encoder(JSONEncoder):
	def default(self, o):
		return o.__dict__

if __name__ == "__main__":
	for game in get_all_game_days():
		one = Game(game)
		print(one.jsonify())
	
	#one = Game(get_all_game_days()[0])
	#print(one.jsonify())
	#print(get_all_game_days())
