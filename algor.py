from game import *

two_weight = 30

def m_one(team) -> tuple:
    sear = team['pitcher']['s_ERA']
    ra = team["RA/G"]

    sip = team['pitcher']['s_IP']

    return (float(ra) - sear, sip['five'] + sip['seven'] * (1.2))

def m_two(team) -> tuple:
    rs = team['RS/G']
    ra = team['RA/G']

    return (float(rs) - float(ra), two_weight)

def algor(game: Game) -> tuple:
    #home team has a 8.11% advantage, given by historical data

    home = 8.11 / 2 
    away = -8.11 / 2

    h_one = m_one(game.home_team)
    home += h_one[0] * h_one[1]

    a_one = m_one(game.away_team)
    away += a_one[0] * a_one[1]

    h_two = m_two(game.home_team)
    home += h_two[0] * h_two[1]

    a_two = m_two(game.away_team)
    away += a_two[0] * a_two[1]

    return ([game.home_team['name'], home], [game.away_team['name'], away])

def all_print(show_json: bool) -> None:
    for game in get_all_game_days():
        one = Game(game)

        if show_json:
            print(one.jsonify())

        print(algor(one))

def one_print(show_json: bool) -> None:
    one = Game(get_all_game_days()[0])

    if show_json:
        print(one.jsonify())

    print(algor(one))

if __name__ == "__main__":
    #one_print(True)

    all_print(False)
