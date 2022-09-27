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
		self.get_data(page)
		self.get_avg_runs(page)

	def get_avg_runs(self, page: None) -> None:
		data = page.find("div", {"id": "group_1"})
		data = data.find("h2").text
		data = data.replace("(", ")").split(")")
		data.remove(data[2])
		data = data[1:len(data)-1]

		self.away_team["RS/G"] = data[0].split(" ")[0]
		self.home_team["RA/G"] = data[1].split(" ")[0]

		data = page.find("div", {"id": "group_2"})
		data = data.find("h2").text
		data = data.replace("(", ")").split(")")
		data.remove(data[2])
		data = data[1:len(data)-1]

		self.home_team["RS/G"] = data[0].split(" ")[0]
		self.away_team["RA/G"] = data[1].split(" ")[0]

	def get_teams(self, page: None) -> None:
		data = page.findAll("h2")

		pitchers = self.get_pitchers(page)
		ten = self.get_last_ten(page)

		self.home_team = {"name": data[3].text, 
						  "abb": data[4].text.split(" ")[0],
						  "record": ten[2],
						  "last_ten": ten[0],
						  "pitcher": {"name": pitchers[0], 
						  			  "era": pitchers[2][0]}}
		self.away_team = {"name": data[0].text, 
		                  "abb": data[1].text.split(" ")[0],
		                  "record": ten[3],
		                  "last_ten": ten[1],
		                  "pitcher": {"name": pitchers[1], 
		                  			  "era": pitchers[2][1]}}

	def get_data(self, page: None) -> None:
		data = page.findAll("div", {'class': ['table_wrapper']})

		home = data[3].find("div", {'class': ['placeholder']}).next_sibling.next_sibling
		home = BeautifulSoup(home, "html.parser")
		home = home.findAll("td", {'data-stat': 'earned_run_avg'})

		self.home_team["pitcher"]["s_IP"] = {}
		self.away_team["pitcher"]["s_IP"] = {}

		self.home_team["pitcher"]["s_ER"] = {}
		self.away_team["pitcher"]["s_ER"] = {}

		self.home_team["pitcher"]["s_ER"]["seven"] = 0.0
		self.home_team["pitcher"]["s_ER"]["five"] = 0.0
		self.home_team["pitcher"]["s_IP"]["seven"] = 0.0
		self.home_team["pitcher"]["s_IP"]["five"] = 0.0

		self.away_team["pitcher"]["s_ER"]["seven"] = 0.0
		self.away_team["pitcher"]["s_ER"]["five"] = 0.0
		self.away_team["pitcher"]["s_IP"]["seven"] = 0.0
		self.away_team["pitcher"]["s_IP"]["five"] = 0.0


		for item in home:
			adult = item.parent.findChildren()
			if "Last" in adult[0].text:
				if "5" in adult[0].text:
					self.home_team["pitcher"]["s_IP"]["five"] = float(adult[3].text)
					self.home_team["pitcher"]["s_ER"]["five"] = float(adult[6].text)
				elif "7" in adult[0].text:
					self.home_team["pitcher"]["s_IP"]["seven"] = float(adult[3].text)
					self.home_team["pitcher"]["s_ER"]["seven"] = float(adult[6].text)


		away = data[1].find("div", {'class': ['placeholder']}).next_sibling.next_sibling
		away = BeautifulSoup(away, "html.parser")
		away = away.findAll("td", {'data-stat': 'earned_run_avg'})

		for item in away:
			adult = item.parent.findChildren()
			if "Last" in adult[0].text:
				if "5" in adult[0].text:
					self.away_team["pitcher"]["s_IP"]["five"] = float(adult[3].text)
					self.away_team["pitcher"]["s_ER"]["five"] = float(adult[6].text)
				elif "7" in adult[0].text:
					self.away_team["pitcher"]["s_IP"]["seven"] = float(adult[3].text)
					self.away_team["pitcher"]["s_ER"]["seven"] = float(adult[6].text)

		if (self.home_team["pitcher"]["s_IP"]["five"] + self.home_team["pitcher"]["s_IP"]["seven"]) == 0:
			self.home_team["pitcher"]["s_ERA"] = 0
		elif (self.away_team["pitcher"]["s_IP"]["five"] + self.away_team["pitcher"]["s_IP"]["seven"]) == 0:
			self.away_team["pitcher"]["s_ERA"] = 0
		else:
			self.home_team["pitcher"]["s_ERA"] =((self.home_team["pitcher"]["s_ER"]["five"] + 
											self.home_team["pitcher"]["s_ER"]["seven"]) * 9) / (self.home_team["pitcher"]["s_IP"]["five"] + 
											 self.home_team["pitcher"]["s_IP"]["seven"])
			self.away_team["pitcher"]["s_ERA"] =((self.away_team["pitcher"]["s_ER"]["five"] + 
											self.away_team["pitcher"]["s_ER"]["seven"]) * 9) / (self.away_team["pitcher"]["s_IP"]["five"] + 
											 self.away_team["pitcher"]["s_IP"]["seven"])

		

	def get_last_ten(self, page: None) -> tuple:
		data = page.findAll("td", text = "Last 10")
		record = page.findAll("td", text = "Record")

		#(home, away)
		return (data[1].next_sibling.next_sibling.text, data[0].next_sibling.next_sibling.text, 
			record[1].next_sibling.next_sibling.text, record[0].next_sibling.next_sibling.text)

	def get_pitchers(self, page: None) -> tuple:
		data = page.findAll("h2")

		if len(data) != 18:
			return (-1, -1, [-1, -1])

		home = data[5].text

		away = data[2].text

		eras = self.find_era(home, away)

		#(home, away)
		return (home.split(" (")[0], away.split(" (")[0], eras)

	def find_era(self, home: str, away: str) -> list:
		home = home.replace(")", ", ").split(", ")
		away = away.replace(")", ", ").split(", ")

		if home[4] == "":
			home = home[3]
		else:
			home = home[4]

		if away[4] == "":
			away = away[3]
		else:
			away = away[4]

		#[home, away]
		return [home, away]
		
		
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
