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

		pitchers = self.get_pitchers(page)
		ten = self.get_last_ten(page)

		self.home_team = {"name": data[3].text, 
						  "abb": data[4].text.split(" ")[0],
						  "last_ten": ten[0],
						  "pitcher": pitchers[0]}
		self.away_team = {"name": data[0].text, 
		                  "abb": data[1].text.split(" ")[0],
		                  "last_ten": ten[1],
		                  "pitcher": pitchers[1]}

	def get_last_ten(self, page: None) -> tuple:
		data = page.findAll("td", text = "Last 10")

		#(home, away)
		return (data[1].next_sibling.next_sibling.text, data[0].next_sibling.next_sibling.text)

	def get_pitchers(self, page: None) -> tuple:
		data = page.findAll("h2")

		#(home, away)
		return (data[5].text.split(" (")[0], data[2].text.split(" (")[0])
		
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
