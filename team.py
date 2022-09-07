import re
import requests
import json
from bs4 import BeautifulSoup
from json import JSONEncoder

class Team:
	def __init__(self, abbreviation: str) -> None:
		self.abbreviation = abbreviation
		self.url = "https://www.baseball-reference.com/teams/" + self.abbreviation + "/2022.shtml"
		page = self.get_parsed_page(self.url)
		s_page = self.get_parsed_page("https://www.baseball-reference.com/teams/" + self.abbreviation + "/2022-schedule-scores.shtml")

		self.name = self.get_name(page)
		self.win_to_loss = self.get_win_to_loss(page)
		self.home_vs_road = self.get_home_vs_road(s_page)
		self.isGameDay = self.get_game_day()

	def get_parsed_page(self, url: str) -> None:
		headers = {
			"referer": "https://baseball-reference.com",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
		}

		return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

	def jsonify(self) -> str:
		return json.dumps(self, indent=4,cls=Encoder)

	def get_win_to_loss(self, page: None) -> float:
		data = page.find("strong", text="Record:").next_sibling

		data = "".join(data.split())
		data = data.split(",")[0].split("-")
		per = int(data[0]) / (int(data[0]) + int(data[1]))

		return per

	def get_home_vs_road(self, page: None) -> tuple:
		data = page.find("div", {"id": "win_loss_sh"}).next_sibling

		data = BeautifulSoup(data, "html.parser")

		home = data.find("td", text = "Home").parent.findChildren()[5].text
		away = data.find("td", text = "Road").parent.findChildren()[5].text


		return (home, away)

	def get_name(self, page: None) -> str:
		data = page.find("span", {"class": ["header_end"], }).find_previous_sibling("span").text

		return data

	def get_game_day(self) -> bool:
		teams = get_all_game_days()

		if self.abbreviation in teams:
			return True
		return False

def get_active_players(team: Team) -> str:
	page = team.get_parsed_page(team.url)
	ret = []

	data = page.find("div", attrs={"id": "all_the40man"})
	data = data.find("div", {"class": "placeholder"}).next_sibling.next_sibling

	data = BeautifulSoup(data, "html.parser")

	data = data.find("table").find_all("tr")
	data = data[1:len(data)-1] #gives all rows, not including first and last

	for player in data:
		if player.find("td", {"data-stat": "is_active"}).text == '*':
			ret.append(player.find("td", {"class": "left"})['csk'])

	return ret

class Encoder(JSONEncoder):
	def default(self, o):
		return o.__dict__

if __name__ == "__main__":
	team = Team("ATL")
	print(team.jsonify())
